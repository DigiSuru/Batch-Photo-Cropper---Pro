# Batch Photo Cropper Pro

A professional, high-performance, browser-based tool for bulk image cropping and processing. Designed with a premium UI/UX, this tool allows users to crop, rotate, apply visual filters, and bulk-export images into a ZIP archive—all completely client-side.

## ✨ Features

- **Bulk Processing**: Upload multiple images and process them sequentially without reloading the page.
- **Advanced UI/UX**: Includes a sleek dark mode theme (Ocean/Teal), ambient glowing background orbs, satisfying micro-interactions, and a custom toast notification system.
- **Drag-and-Drop**: Easily upload images by dragging them directly onto the upload zone.
- **Keyboard Shortcuts**: Power users can use `[↵]` (Enter) to Crop & Next, and `[S]` to Skip the current image.
- **Live Preview**: See exact square and circular previews of your crop in real-time.
- **Custom Export Settings**:
  - Choose between multiple Aspect Ratios (Passport, Square, Portrait, Freehand).
  - Define custom pixel resolution limits.
  - Select output formats (JPEG, PNG, WEBP) and adjust compression quality.
  - Enable custom filename patterns (e.g., `{name}_cropped_{index}`).
- **Hardware-Accelerated Filters**: Live adjustments for Brightness, Contrast, Saturation, and Rotation.
- **Privacy First**: Everything runs entirely in your browser using local resources. No images are uploaded to any server.

## 🛠️ Technology Stack

- **HTML5 & Vanilla JavaScript**: Core structure and logic.
- **Tailwind CSS**: Styling and responsive design (via CDN).
- **Cropper.js**: Robust canvas-based image cropping engine.
- **JSZip & FileSaver.js**: For bundling the processed images and triggering the local download.

## 🚀 How to Use

1. **Upload**: Click the upload area or drag-and-drop a batch of images (JPG, PNG, WEBP).
2. **Crop & Edit**: 
   - Use your mouse to adjust the crop box.
   - Use the sliders to adjust brightness, contrast, and saturation.
   - Press `Enter` to confirm the crop and move to the next image, or press `S` to skip.
3. **Export**: Once all images are processed, click **Download ZIP Archive** to save your files locally.

## 👨‍💻 Credits

Made with Love by [SK Meghwal](https://skmeghwal.in)