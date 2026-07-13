# Batch-Photo-Cropper---Pro

A lightweight, browser-based, client-side tool designed to bulk crop and resize student photos for official board forms, ID cards, and passports.
Because this tool processes everything directly in your web browser, no images are ever uploaded to an external server. This guarantees 100% privacy and security for student data.
🚀 Key Features
Privacy First: 100% offline processing. No backend server required.
Bulk Processing: Select dozens or hundreds of photos at once and cycle through them seamlessly.
Precision Aspect Ratios: Pre-configured for standard ID sizes (like 3.5 x 4.5) with custom inputs available.
Exact Output Sizes: Define exact output dimensions (e.g., 350x450px) or set a maximum file dimension to adhere to strict form requirements.
Advanced Image Adjustments:
Rotate (90° steps or micro-tilt adjustments for crooked photos).
Flip (Horizontal/Vertical).
Zoom & Pan.
Format & Quality Control: Export as JPEG, PNG, or WebP. Adjust JPEG/WebP compression quality to meet strict file size limits (e.g., "Must be under 50kb").
Speed Workflow: Keyboard shortcut (Enter key) to quickly crop and jump to the next photo.
Zip Export: Automatically bundles all finished, correctly sized photos into a single .zip file for easy downloading.
🛠️ How to Use
Step 1: Configuration
Open the HTML file in any modern web browser (Chrome, Edge, Safari, Firefox).
Crop Aspect Ratio: Select a preset (e.g., 3.5 : 4.5) or choose "Custom" to set your own.
Output Size: * Choose "Original Size" to keep the cropped area at its maximum resolution.
Choose "Specific Dimensions" if the board form requires exact pixels (e.g., exactly 350px by 450px).
Choose "Max Width/Height" if the form specifies a maximum bound (e.g., max 800px wide).
Output Format: Select your required image format and adjust the quality slider to control the final file size.
Step 2: Upload
Click the "Select Photos" button and choose all the student photos you captured from your phone or computer.
Step 3: Crop and Adjust
The tool will present the first photo. The crop box is locked to your chosen aspect ratio.
Drag, zoom, or use the Adjustment Tools (Rotate, Flip, Tilt) to perfectly align the student's face.
Click "Crop & Next" (or press the Enter key on your keyboard) to save the crop and instantly move to the next student.
Mistake? Use the "Previous" button to go back and re-crop.
Step 4: Download
Once you crop the final photo, the tool will automatically package all the processed files into a single ZIP archive (cropped_photos.zip) and download it to your device. The individual files inside will have cropped_ prefixed to their original names.
💻 Tech Stack
This tool is built entirely with front-end web technologies in a single file:
HTML5 / CSS3 (Tailwind CSS via CDN for styling)
Vanilla JavaScript (Logic and DOM manipulation)
Cropper.js (For the cropping engine and UI)
JSZip (For generating the final zip file)
🔒 Security Note
This tool can be run entirely offline. Once the page is loaded, you can disconnect from the internet and the tool will continue to function perfectly. No data ever leaves your device.