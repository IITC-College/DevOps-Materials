#!/bin/bash
################################################################################
# Setup Environment Script for Lab: Network Adapter Debug
#
# Creates ONE specific networking "bug" for ONE clue. Run BEFORE each clue so
# the student has that exact issue to diagnose and fix.
#
# Usage: sudo ./setup_environment.sh <level> <clue>
#   Example: sudo ./setup_environment.sh 1 1   (before Level 1, Clue 1)
#   Example: sudo ./setup_environment.sh 2 2   (before Level 2, Clue 2)
#
# Scenarios:
#   Level 1 (Basic - Link layer):
#     1-1: Interface DOWN
#     1-2: Interface UP but no IP address
#     1-3: Missing default gateway
#
#   Level 2 (Intermediate - Services/Firewall):
#     2-1: DNS misconfigured (bad /etc/resolv.conf)
#     2-2: UFW blocking incoming SSH (port 22)
#     2-3: UFW blocking outgoing HTTP/HTTPS (80/443)
#
#   Level 3 (Advanced - Complex):
#     3-1: Wrong MTU (500) causing large packet failures
#     3-2: Static route missing/wrong for specific subnet
#     3-3: /etc/hosts overriding DNS with wrong IP
#
# IMPORTANT: Run from VM console for scenarios that may drop SSH (1-1, 2-2).
################################################################################

set -e

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

LEVEL="${1:?Usage: sudo ./setup_environment.sh <level> <clue>   (level 1-3, clue 1-3)}"
CLUE="${2:?Usage: sudo ./setup_environment.sh <level> <clue>   (level 1-3, clue 1-3)}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LOGS_DIR="$SCRIPT_DIR/data/logs"
BACKUP_DIR="$SCRIPT_DIR/data/backups"

echo -e "${BLUE}╔════════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║  Network Adapter Lab - Create bug for Level ${LEVEL} Clue ${CLUE}                  ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════════════╝${NC}"
echo ""

if [ "$EUID" -ne 0 ]; then
    echo -e "${YELLOW}Please run with sudo:${NC} sudo ./setup_environment.sh $LEVEL $CLUE"
    exit 1
fi

if [[ ! "$LEVEL" =~ ^[123]$ ]] || [[ ! "$CLUE" =~ ^[123]$ ]]; then
    echo -e "${RED}Invalid arguments. Use level 1-3 and clue 1-3.${NC}"
    exit 1
fi

# First non-loopback interface (enp*, eth*, ens*)
IFACE=$(ip -o link show | awk -F': ' '{print $2}' | grep -v '^lo$' | grep -E '^(enp|eth|ens)' | head -1)
if [ -z "$IFACE" ]; then
    echo -e "${RED}No suitable interface found (enp*, eth*, ens*).${NC}"
    exit 1
fi

# Get current gateway
GATEWAY=$(ip route | grep default | awk '{print $3}' | head -1)

echo -e "${GREEN}[INFO]${NC} Target interface: $IFACE"
echo -e "${GREEN}[INFO]${NC} Current gateway: ${GATEWAY:-none}"
echo -e "${GREEN}[INFO]${NC} Creating bug for Level $LEVEL, Clue $CLUE"
echo ""

mkdir -p "$LOGS_DIR" "$BACKUP_DIR"

# Save state before changes
echo -e "${GREEN}[STEP]${NC} Saving current state..."
{
    echo "=== Date: $(date) ==="
    echo "=== Level $LEVEL Clue $CLUE ==="
    echo ""
    echo "=== ip link show ==="
    ip link show
    echo ""
    echo "=== ip addr show ==="
    ip addr show
    echo ""
    echo "=== ip route ==="
    ip route
    echo ""
    echo "=== /etc/resolv.conf ==="
    cat /etc/resolv.conf 2>/dev/null || true
    echo ""
    echo "=== ufw status ==="
    ufw status verbose 2>/dev/null || echo "ufw not installed or not running"
} > "$LOGS_DIR/state_before_${LEVEL}_${CLUE}.txt" 2>&1

# Backup critical files
cp /etc/resolv.conf "$BACKUP_DIR/resolv.conf.bak" 2>/dev/null || true
cp /etc/hosts "$BACKUP_DIR/hosts.bak" 2>/dev/null || true
echo -e "  ${GREEN}✓${NC} State and backups saved to data/"
echo ""

################################################################################
# SCENARIO IMPLEMENTATIONS
################################################################################

case "$LEVEL$CLUE" in

    ############################################################################
    # LEVEL 1: Basic - Link layer issues
    ############################################################################

    11)
        # 1-1: Interface DOWN
        echo -e "${GREEN}[SCENARIO 1-1]${NC} Interface DOWN"
        echo "  Bringing $IFACE down..."
        ip link set "$IFACE" down
        echo -e "${GREEN}✓${NC} $IFACE is now DOWN."
        echo ""
        echo -e "${YELLOW}WARNING:${NC} SSH over $IFACE is lost. Use VM console."
        echo -e "${YELLOW}Fix:${NC} sudo ip link set $IFACE up"
        ;;

    12)
        # 1-2: Interface UP but no IP address
        echo -e "${GREEN}[SCENARIO 1-2]${NC} Interface UP but no IP address"
        echo "  Ensuring $IFACE is up..."
        ip link set "$IFACE" up 2>/dev/null || true
        echo "  Flushing all IP addresses from $IFACE..."
        ip addr flush dev "$IFACE"
        echo -e "${GREEN}✓${NC} $IFACE is UP but has no IP address."
        echo ""
        echo -e "${YELLOW}Fix:${NC} sudo dhclient $IFACE  OR  sudo ip addr add <ip>/<mask> dev $IFACE"
        ;;

    13)
        # 1-3: Missing default gateway
        echo -e "${GREEN}[SCENARIO 1-3]${NC} Missing default gateway"
        echo "  Ensuring interface is up with IP..."
        ip link set "$IFACE" up 2>/dev/null || true
        if ! ip addr show "$IFACE" | grep -q 'inet '; then
            dhclient "$IFACE" 2>/dev/null || true
            sleep 2
        fi
        echo "  Removing default gateway..."
        ip route del default 2>/dev/null || true
        echo -e "${GREEN}✓${NC} Default gateway removed. Local network works, internet doesn't."
        echo ""
        echo -e "${YELLOW}Fix:${NC} sudo ip route add default via <gateway_ip>"
        ;;

    ############################################################################
    # LEVEL 2: Intermediate - Services/Firewall issues
    ############################################################################

    21)
        # 2-1: DNS misconfigured (bad /etc/resolv.conf)
        echo -e "${GREEN}[SCENARIO 2-1]${NC} DNS misconfigured"
        echo "  Ensuring network connectivity first..."
        ip link set "$IFACE" up 2>/dev/null || true
        if ! ip addr show "$IFACE" | grep -q 'inet '; then
            dhclient "$IFACE" 2>/dev/null || true
            sleep 2
        fi
        if [ -z "$(ip route | grep default)" ]; then
            [ -n "$GATEWAY" ] && ip route add default via "$GATEWAY" 2>/dev/null || true
        fi
        echo "  Breaking DNS by setting invalid nameserver..."
        # Backup and replace resolv.conf
        echo "# Broken DNS - invalid nameserver" > /etc/resolv.conf
        echo "nameserver 192.0.2.1" >> /etc/resolv.conf
        echo "nameserver 198.51.100.1" >> /etc/resolv.conf
        echo -e "${GREEN}✓${NC} DNS broken. ping by IP works, but ping by hostname fails."
        echo ""
        echo -e "${YELLOW}Test:${NC} ping 8.8.8.8 (works) vs ping google.com (fails)"
        echo -e "${YELLOW}Fix:${NC} Edit /etc/resolv.conf with valid nameserver (e.g., 8.8.8.8)"
        ;;

    22)
        # 2-2: UFW blocking incoming SSH (port 22)
        echo -e "${GREEN}[SCENARIO 2-2]${NC} UFW blocking incoming SSH"
        echo "  Ensuring network is up..."
        ip link set "$IFACE" up 2>/dev/null || true
        if ! ip addr show "$IFACE" | grep -q 'inet '; then
            dhclient "$IFACE" 2>/dev/null || true
            sleep 2
        fi
        echo "  Enabling UFW and blocking SSH..."
        ufw --force reset >/dev/null 2>&1 || true
        ufw default allow outgoing >/dev/null 2>&1
        ufw default deny incoming >/dev/null 2>&1
        ufw --force enable >/dev/null 2>&1
        # SSH is now blocked (deny incoming, no allow rule for 22)
        echo -e "${GREEN}✓${NC} UFW enabled, incoming SSH (port 22) is blocked."
        echo ""
        echo -e "${YELLOW}WARNING:${NC} New SSH connections will fail. Use VM console."
        echo -e "${YELLOW}Test:${NC} sudo ufw status"
        echo -e "${YELLOW}Fix:${NC} sudo ufw allow ssh  OR  sudo ufw allow 22/tcp"
        ;;

    23)
        # 2-3: UFW blocking outgoing HTTP/HTTPS (ports 80/443)
        echo -e "${GREEN}[SCENARIO 2-3]${NC} UFW blocking outgoing HTTP/HTTPS"
        echo "  Ensuring network is up..."
        ip link set "$IFACE" up 2>/dev/null || true
        if ! ip addr show "$IFACE" | grep -q 'inet '; then
            dhclient "$IFACE" 2>/dev/null || true
            sleep 2
        fi
        echo "  Configuring UFW to block outgoing web traffic..."
        ufw --force reset >/dev/null 2>&1 || true
        ufw default deny outgoing >/dev/null 2>&1
        ufw default allow incoming >/dev/null 2>&1
        ufw allow out 22/tcp >/dev/null 2>&1    # Allow SSH out
        ufw allow out 53 >/dev/null 2>&1        # Allow DNS out
        ufw allow out to any port 123 >/dev/null 2>&1  # Allow NTP
        # HTTP/HTTPS (80, 443) NOT allowed
        ufw --force enable >/dev/null 2>&1
        echo -e "${GREEN}✓${NC} UFW blocks outgoing HTTP (80) and HTTPS (443)."
        echo ""
        echo -e "${YELLOW}Test:${NC} curl http://example.com (fails), ping 8.8.8.8 (may work)"
        echo -e "${YELLOW}Fix:${NC} sudo ufw allow out 80/tcp && sudo ufw allow out 443/tcp"
        ;;

    ############################################################################
    # LEVEL 3: Advanced - Complex issues
    ############################################################################

    31)
        # 3-1: Wrong MTU causing large packet failures
        echo -e "${GREEN}[SCENARIO 3-1]${NC} Wrong MTU (500)"
        echo "  Ensuring network is fully up..."
        ip link set "$IFACE" up 2>/dev/null || true
        if ! ip addr show "$IFACE" | grep -q 'inet '; then
            dhclient "$IFACE" 2>/dev/null || true
            sleep 2
        fi
        if [ -z "$(ip route | grep default)" ]; then
            [ -n "$GATEWAY" ] && ip route add default via "$GATEWAY" 2>/dev/null || true
        fi
        # Restore DNS if broken
        if grep -q '192.0.2.1' /etc/resolv.conf 2>/dev/null; then
            echo "nameserver 8.8.8.8" > /etc/resolv.conf
        fi
        echo "  Setting MTU to 500 (way too low)..."
        ip link set "$IFACE" mtu 500
        echo -e "${GREEN}✓${NC} MTU set to 500. Small pings work, large transfers fail."
        echo ""
        echo -e "${YELLOW}Test:${NC} ping -c 1 8.8.8.8 (works), ping -s 1000 8.8.8.8 (fails or fragments)"
        echo -e "${YELLOW}Fix:${NC} sudo ip link set $IFACE mtu 1500"
        ;;

    32)
        # 3-2: Static route missing/wrong for specific subnet
        echo -e "${GREEN}[SCENARIO 3-2]${NC} Wrong static route"
        echo "  Ensuring network is fully up..."
        ip link set "$IFACE" up 2>/dev/null || true
        if ! ip addr show "$IFACE" | grep -q 'inet '; then
            dhclient "$IFACE" 2>/dev/null || true
            sleep 2
        fi
        if [ -z "$(ip route | grep default)" ]; then
            [ -n "$GATEWAY" ] && ip route add default via "$GATEWAY" 2>/dev/null || true
        fi
        # Restore DNS if broken
        if grep -q '192.0.2.1' /etc/resolv.conf 2>/dev/null; then
            echo "nameserver 8.8.8.8" > /etc/resolv.conf
        fi
        ip link set "$IFACE" mtu 1500 2>/dev/null || true
        echo "  Adding wrong route for 8.8.8.0/24 (Google DNS subnet)..."
        ip route del 8.8.8.0/24 2>/dev/null || true
        ip route add 8.8.8.0/24 via 127.0.0.1 2>/dev/null || \
        ip route add blackhole 8.8.8.0/24 2>/dev/null || true
        echo -e "${GREEN}✓${NC} Route to 8.8.8.0/24 points to wrong destination."
        echo ""
        echo -e "${YELLOW}Test:${NC} ping 1.1.1.1 (works), ping 8.8.8.8 (fails)"
        echo -e "${YELLOW}Inspect:${NC} ip route"
        echo -e "${YELLOW}Fix:${NC} sudo ip route del 8.8.8.0/24 && sudo ip route add 8.8.8.0/24 via <gateway>"
        ;;

    33)
        # 3-3: /etc/hosts overriding DNS with wrong IP
        echo -e "${GREEN}[SCENARIO 3-3]${NC} /etc/hosts overriding DNS"
        echo "  Ensuring network is fully up..."
        ip link set "$IFACE" up 2>/dev/null || true
        if ! ip addr show "$IFACE" | grep -q 'inet '; then
            dhclient "$IFACE" 2>/dev/null || true
            sleep 2
        fi
        if [ -z "$(ip route | grep default)" ]; then
            [ -n "$GATEWAY" ] && ip route add default via "$GATEWAY" 2>/dev/null || true
        fi
        # Restore DNS if broken
        if grep -q '192.0.2.1' /etc/resolv.conf 2>/dev/null; then
            echo "nameserver 8.8.8.8" > /etc/resolv.conf
        fi
        ip link set "$IFACE" mtu 1500 2>/dev/null || true
        ip route del 8.8.8.0/24 2>/dev/null || true
        ip route del blackhole 8.8.8.0/24 2>/dev/null || true
        echo "  Adding wrong entry in /etc/hosts for google.com..."
        # Remove old bad entries if any
        sed -i '/google.com/d' /etc/hosts 2>/dev/null || true
        echo "127.0.0.1   google.com www.google.com" >> /etc/hosts
        echo -e "${GREEN}✓${NC} /etc/hosts maps google.com to 127.0.0.1"
        echo ""
        echo -e "${YELLOW}Test:${NC} ping google.com (goes to 127.0.0.1), ping 142.250.x.x (works)"
        echo -e "${YELLOW}Inspect:${NC} cat /etc/hosts, getent hosts google.com"
        echo -e "${YELLOW}Fix:${NC} Remove the bad line from /etc/hosts"
        ;;

    *)
        echo -e "${RED}Invalid level/clue combination.${NC}"
        exit 1
        ;;
esac

echo ""
echo -e "${BLUE}Done.${NC} Student works on clues/level${LEVEL}/clue${CLUE}.txt"
echo ""
