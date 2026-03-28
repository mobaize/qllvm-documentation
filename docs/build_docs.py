#!/usr/bin/env python
"""
Build script for QLLVM documentation
Supports building both Chinese and English versions
"""

import subprocess
import shutil
import os
import sys
import time

# Get the directory of this script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SOURCE_DIR = os.path.join(SCRIPT_DIR, 'source')
BUILD_DIR = os.path.join(SCRIPT_DIR, 'build')
HTML_DIR = os.path.join(BUILD_DIR, 'html')

def clean_build():
    """Clean the build directory"""
    if os.path.exists(BUILD_DIR):
        try:
            # 尝试多次删除
            for i in range(3):
                try:
                    shutil.rmtree(BUILD_DIR)
                    print("Build directory cleaned.")
                    break
                except PermissionError:
                    if i < 2:
                        print(f"Retrying clean ({i+1}/3)...")
                        time.sleep(1)
                    else:
                        print("Warning: Could not clean build directory. It may be in use.")
                        print("Continuing with existing build...")
        except Exception as e:
            print(f"Warning: Error cleaning build directory: {e}")
            print("Continuing with existing build...")
    else:
        print("Build directory does not exist.")

def build_chinese():
    """Build Chinese documentation"""
    print("\n=== Building Chinese Documentation ===")
    
    # Create a temporary conf file for Chinese
    conf_path = os.path.join(SOURCE_DIR, 'conf.py')
    with open(conf_path, 'r', encoding='utf-8') as f:
        conf_content = f.read()
    
    # Ensure language is set to Chinese
    conf_content = conf_content.replace("language = 'en'", "language = 'zh_CN'")
    
    with open(conf_path, 'w', encoding='utf-8') as f:
        f.write(conf_content)
    
    print("Language set to zh_CN")
    
    # Build Chinese docs
    result = subprocess.run(
        ['sphinx-build', '-b', 'html', SOURCE_DIR, HTML_DIR],
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0:
        print("Error building Chinese docs:")
        print(result.stderr)
        return False
    
    print("Chinese documentation built successfully.")
    return True

def build_english():
    """Build English documentation"""
    print("\n=== Building English Documentation ===")
    
    # Create a temporary conf file for English
    conf_path = os.path.join(SOURCE_DIR, 'conf.py')
    with open(conf_path, 'r', encoding='utf-8') as f:
        conf_content = f.read()
    
    # Change language to English
    conf_content = conf_content.replace("language = 'zh_CN'", "language = 'en'")
    
    with open(conf_path, 'w', encoding='utf-8') as f:
        f.write(conf_content)
    
    print("Language set to en")
    
    # Build English docs to a temporary directory
    en_build_dir = os.path.join(BUILD_DIR, 'html_en')
    
    # Clean up English build directory if it exists
    if os.path.exists(en_build_dir):
        try:
            shutil.rmtree(en_build_dir)
        except PermissionError:
            print(f"Warning: Could not clean {en_build_dir}")
    
    result = subprocess.run(
        ['sphinx-build', '-b', 'html', SOURCE_DIR, en_build_dir],
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0:
        print("Error building English docs:")
        print(result.stderr)
        return False
    
    # Copy English files to the main html directory
    for root, dirs, files in os.walk(en_build_dir):
        for file in files:
            if file.endswith('.html'):
                src_path = os.path.join(root, file)
                rel_path = os.path.relpath(src_path, en_build_dir)
                dst_path = os.path.join(HTML_DIR, rel_path)
                
                # Ensure destination directory exists
                os.makedirs(os.path.dirname(dst_path), exist_ok=True)
                shutil.copy2(src_path, dst_path)
    
    # Clean up temporary directory
    try:
        shutil.rmtree(en_build_dir)
    except PermissionError:
        print(f"Warning: Could not clean up {en_build_dir}")
    
    print("English documentation built successfully.")
    return True

def main():
    """Main function"""
    # Clean build directory
    clean_build()
    
    # Build Chinese docs
    if not build_chinese():
        print("Failed to build Chinese documentation.")
        sys.exit(1)
    
    # Build English docs
    if not build_english():
        print("Failed to build English documentation.")
        sys.exit(1)
    
    print("\n=== Build Complete ===")
    print(f"Documentation built in: {HTML_DIR}")
    print("Chinese: index.html")
    print("English: index.en.html")

if __name__ == '__main__':
    main()
