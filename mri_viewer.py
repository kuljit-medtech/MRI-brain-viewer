# Import the libraries we installed
import nibabel as nib
import matplotlib.pyplot as plt
from nilearn import datasets
import numpy as np

# Step 1: Download a sample MRI brain scan
print("Downloading sample MRI brain scan...")
dataset = datasets.fetch_icbm152_2009()
mri_file = dataset.t1

# Step 2: Load the MRI file
print("Loading MRI file...")
img = nib.load(mri_file)

# Step 3: Get the image data as numbers
data = img.get_fdata()
print("MRI scan shape:", data.shape)
print("Total slices available - X:", data.shape[0], "Y:", data.shape[1], "Z:", data.shape[2])

# Step 4: Display 3 slices of the brain
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].imshow(data[90, :, :], cmap='gray', origin='lower')
axes[0].set_title('Sagittal View (Side)', fontsize=13)
axes[0].set_xlabel('Z axis')
axes[0].set_ylabel('Y axis')

axes[1].imshow(data[:, 108, :], cmap='gray', origin='lower')
axes[1].set_title('Coronal View (Front)', fontsize=13)
axes[1].set_xlabel('Z axis')
axes[1].set_ylabel('X axis')

axes[2].imshow(data[:, :, 90], cmap='gray', origin='lower')
axes[2].set_title('Axial View (Top)', fontsize=13)
axes[2].set_xlabel('Y axis')
axes[2].set_ylabel('X axis')

plt.suptitle('MRI Brain Viewer - ICBM152 Template', fontsize=16)
plt.tight_layout()
plt.show()
print("Done!")