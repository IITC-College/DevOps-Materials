#!/bin/bash
################################################################################
# Restore script - Fixes ALL issues and returns system to normal state
# Run this after the lab or if things go wrong
################################################################################

set -e

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}╔════════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║  Restoring system to normal state                                  ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════════════╝${NC}"
echo ""

if [ "$EUID" -ne 0 ]; then
    echo -e "${YELLOW}Please run with sudo:${NC} sudo ./restore_all.sh"
    exit 1
fi

# Find interface
IFACE=$(ip -o link show | awk -F': ' '{print $2}' | grep -v '^lo$' | grep -E '^(enp|eth|ens)' | head -1)

echo -e "${GREEN}[1/7]${NC} Bringing interface up..."
ip link set "$IFACE" up 2>/dev/null || true

echo -e "${GREEN}[2/7]${NC} Getting IP via DHCP..."
dhclient "$IFACE" 2>/dev/null || true

echo -e "${GREEN}[3/7]${NC} Setting MTU to 1500..."
ip link set "$IFACE" mtu 1500 2>/dev/null || true

echo -e "${GREEN}[4/7]${NC} Removing bad routes..."
ip route del 8.8.8.0/24 2>/dev/null || true
ip route del blackhole 8.8.8.0/24 2>/dev/null || true

echo -e "${GREEN}[5/7]${NC} Fixing /etc/hosts..."
sed -i '/google.com/d' /etc/hosts 2>/dev/null || true

echo -e "${GREEN}[6/7]${NC} Fixing DNS..."
echo "nameserver 8.8.8.8" > /etc/resolv.conf
echo "nameserver 8.8.4.4" >> /etc/resolv.conf

echo -e "${GREEN}[7/7]${NC} Resetting UFW..."
ufw --force reset >/dev/null 2>&1 || true
ufw default allow outgoing >/dev/null 2>&1 || true
ufw default deny incoming >/dev/null 2>&1 || true
ufw allow ssh >/dev/null 2>&1 || true
ufw --force enable >/dev/null 2>&1 || true

echo ""
echo -e "${GREEN}✓${NC} System restored to normal state!"
echo ""
echo "Verification:"
echo "  ip link show $IFACE"
echo "  ip addr show $IFACE"
echo "  ip route"
echo "  ping -c 2 8.8.8.8"
echo "  ping -c 2 google.com"
echo ""
