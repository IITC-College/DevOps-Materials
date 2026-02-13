#!/usr/bin/env python3
# try/except/finally clause

"""
TRY/EXCEPT/FINALLY:

try:
    risky_code()
except ErrorType:
    handle_error()
finally:
    # ALWAYS runs (cleanup code)
    cleanup()

FINALLY block runs no matter what!
- Exception or no exception
- Return or no return
- Perfect for cleanup
"""

# Example 1: finally always runs
print("Example 1: finally always executes")
print("-" * 40)

def test_finally(will_fail):
    """Demonstrate finally execution"""
    try:
        if will_fail:
            result = 10 / 0
        else:
            result = 10 / 2
            print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error caught")
    finally:
        print("Finally: Always runs!")

print("Success case:")
test_finally(False)
print("\nError case:")
test_finally(True)

# Example 2: Cleanup with finally
print("\nExample 2: Resource cleanup")
print("-" * 40)

def process_file_with_cleanup(filename):
    """Process file with cleanup"""
    file_handle = None
    try:
        print(f"Opening {filename}...")
        file_handle = open(filename, 'r')
        data = file_handle.read()
        print(f"Read {len(data)} characters")
        return data
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return None
    finally:
        print("Cleanup: Closing file handle...")
        if file_handle:
            file_handle.close()
            print("  ✓ File closed")

# Create test file
with open('data.txt', 'w') as f:
    f.write("Test data")

result = process_file_with_cleanup('data.txt')
print()
result = process_file_with_cleanup('missing.txt')

# Example 3: try/except/else/finally together
print("\nExample 3: Complete structure")
print("-" * 40)

def complete_example(filename):
    """All clauses together"""
    print(f"1. Starting operation on {filename}")
    
    try:
        print("2. Try block: opening file...")
        with open(filename, 'r') as f:
            data = f.read()
    except FileNotFoundError:
        print("3. Except block: handling error")
        return None
    else:
        print("3. Else block: success!")
        print(f"   Data length: {len(data)}")
        return data
    finally:
        print("4. Finally block: cleanup (always runs)")

result = complete_example('data.txt')
print()
result = complete_example('missing.txt')

# Example 4: finally with return
print("\nExample 4: finally runs even with return")
print("-" * 40)

def function_with_return():
    """Finally runs even if function returns"""
    try:
        print("Try block")
        return "returning from try"
    finally:
        print("Finally block (runs even with return!)")

result = function_with_return()
print(f"Result: {result}")

# Example 5: Database connection pattern
print("\nExample 5: Connection cleanup pattern")
print("-" * 40)

class FakeDatabase:
    def __init__(self):
        self.connected = False
    
    def connect(self):
        print("  DB: Connecting...")
        self.connected = True
    
    def query(self, sql):
        if not self.connected:
            raise Exception("Not connected")
        print(f"  DB: Executing {sql}")
        return ["result1", "result2"]
    
    def disconnect(self):
        print("  DB: Disconnecting...")
        self.connected = False

def database_operation():
    """Database operation with guaranteed cleanup"""
    db = FakeDatabase()
    try:
        db.connect()
        results = db.query("SELECT * FROM users")
        print(f"✓ Got {len(results)} results")
        return results
    except Exception as e:
        print(f"✗ Error: {e}")
        return None
    finally:
        print("Cleanup:")
        db.disconnect()

results = database_operation()

# Example 6: Nested try/finally
print("\nExample 6: Multiple resources")
print("-" * 40)

def multi_resource_operation():
    """Handle multiple resources"""
    file1 = None
    file2 = None
    
    try:
        file1 = open('data.txt', 'r')
        print("✓ Opened file1")
        
        file2 = open('output.txt', 'w')
        print("✓ Opened file2")
        
        # Process
        data = file1.read()
        file2.write(data.upper())
        print("✓ Processed data")
        
    finally:
        print("Cleanup:")
        if file1:
            file1.close()
            print("  ✓ Closed file1")
        if file2:
            file2.close()
            print("  ✓ Closed file2")

multi_resource_operation()

print("\nKey points:")
print("  ✓ finally always runs")
print("  ✓ Perfect for cleanup code")
print("  ✓ Runs even if return/break/continue")
print("  ✓ Runs even if exception not caught")
print("  ✓ Use for closing files, connections, etc.")
