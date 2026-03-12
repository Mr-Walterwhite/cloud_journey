#!/usr/bin/env python3
# File Organizer - automatically sorts files by type

import os
import shutil

# Define file categories
categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx"],
    "Audio": [".mp3", ".wav", ".flac", ".aac"],
    "Code": [".py", ".js", ".html", ".css", ".sh", ".java"],
    "Archives": [".zip", ".tar", ".gz", ".rar"],
}

def get_category(extension):
    for category, extensions in categories.items():
        if extension.lower() in extensions:
            return category
    return "Others"

def organize_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist")
        return

    files = os.listdir(folder_path)
    moved = 0
    skipped = 0

    print(f"\n📂 Organizing: {folder_path}")
    print("=" * 40)

    for filename in files:
        filepath = os.path.join(folder_path, filename)

        # Skip folders
        if os.path.isdir(filepath):
            skipped += 1
            continue

        # Get file extension
        _, extension = os.path.splitext(filename)
        if not extension:
            skipped += 1
            continue

        # Get category
        category = get_category(extension)

        # Create category folder if needed
        category_path = os.path.join(folder_path, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
            print(f"📁 Created folder: {category}")

        # Move file
        destination = os.path.join(category_path, filename)
        shutil.move(filepath, destination)
        print(f"✓ {filename} → {category}/")
        moved += 1

    print("=" * 40)
    print(f"✅ Done! Moved: {moved} files | Skipped: {skipped} items")

# Main
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        folder = sys.argv[1]
    else:
        folder = input("Enter folder path to organize: ")
    
    organize_folder(folder)