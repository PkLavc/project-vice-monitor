#!/usr/bin/env python3
"""
Test script to validate the monitor_new.py fixes
"""

import json
import os
import sys

def test_monitor_new():
    """Test the monitor_new.py script"""
    print("Testing monitor_new.py...")
    
    # Test 1: Check if monitor_new.py can be imported and run
    try:
        import monitor_new
        print("OK: monitor_new.py imports successfully")
    except Exception as e:
        print(f"ERROR: Failed to import monitor_new.py: {e}")
        return False
    
    # Test 2: Check if index.html exists and has correct structure
    if not os.path.exists('index.html'):
        print("ERROR: index.html not found")
        return False
    
    with open('index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Check for key elements that should be present
    required_elements = [
        'id="global-status"',
        'id="last-update-badge"',
        'id="gta-vi-official-sla-24h"',
        'id="gta-vi-official-latency"',
        'id="gta-vi-official-html-size"',
        'id="gta-vi-official-images"',
        'id="gta-vi-official-links"',
        'id="gta-vi-official-scripts"',
        'id="gta-vi-official-title"',
        'id="gta-vi-official-description"'
    ]
    
    for element in required_elements:
        if element in html_content:
            print(f"OK: Found {element}")
        else:
            print(f"ERROR: Missing {element}")
            return False
    
    # Test 3: Check if data directory exists
    if not os.path.exists('data'):
        print("ERROR: data directory not found")
        return False
    
    # Test 4: Check if blog directory exists
    if not os.path.exists('blog'):
        print("ERROR: blog directory not found")
        return False
    
    # Test 5: Check if history.json exists
    if not os.path.exists('history.json'):
        print("ERROR: history.json not found")
        return False
    
    print("OK: All tests passed!")
    return True

def test_data_generation():
    """Test data generation and HTML updates"""
    print("\nTesting data generation...")
    
    try:
        # Import and run the main function
        import monitor_new
        
        # This would normally run the full monitoring, but we'll just test the data processing
        history = monitor_new.load_history()
        print("OK: History loaded successfully")
        
        # Test process_service_data function
        for service_key in monitor_new.SERVICES.keys():
            service_data = monitor_new.process_service_data(history, service_key)
            print(f"OK: Processed data for {service_key}")
            
            # Check if all required fields are present
            required_fields = [
                'current_status', 'sla_24h', 'sla_7d', 'sla_30d',
                'performance', 'html_size_kb', 'num_images', 
                'num_links', 'num_scripts', 'page_title', 'meta_description'
            ]
            
            for field in required_fields:
                if field in service_data:
                    print(f"  OK: {field}: {service_data[field]}")
                else:
                    print(f"  ERROR: Missing {field}")
                    return False
        
        print("OK: Data generation test passed!")
        return True
        
    except Exception as e:
        print(f"ERROR: Data generation test failed: {e}")
        return False

def main():
    """Main test function"""
    print("Project Vice Monitor - Test Suite")
    print("=" * 50)
    
    # Run tests
    test1_passed = test_monitor_new()
    test2_passed = test_data_generation()
    
    print("\n" + "=" * 50)
    if test1_passed and test2_passed:
        print("All tests passed! The system is ready.")
        return 0
    else:
        print("Some tests failed. Please check the errors above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())