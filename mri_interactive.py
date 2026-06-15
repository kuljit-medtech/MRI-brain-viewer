# Import libraries
import nibabel as nib
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from nilearn import datasets
import numpy as np

# Step 1: Load the MRI brain scan
print("Loading MRI brain scan...")
dataset = datasets.fetch_icbm152_2009()
img = nib.load(dataset.t1)
data = img.get_fdata()
print("Scan loaded! Shape:", data.shape)

# Step 2: Set starting slice numbers
slice_x = 90
slice_y = 108
slice_z = 90

# Step 3: Create the figure and 3 image panels
fig, axes = plt.subplots(1, 3, figsize=(15, 6))
plt.subplots_adjust(bottom=0.35)

# Draw the 3 brain views
img_x = axes[0].imshow(data[slice_x, :, :], cmap='gray', origin='lower')
axes[0].set_title('Sagittal View (Side)', fontsize=13)

img_y = axes[1].imshow(data[:, slice_y, :], cmap='gray', origin='lower')
axes[1].set_title('Coronal View (Front)', fontsize=13)

img_z = axes[2].imshow(data[:, :, slice_z], cmap='gray', origin='lower')
axes[2].set_title('Axial View (Top)', fontsize=13)

plt.suptitle('Interactive MRI Brain Viewer', fontsize=16)

# Step 4: Create 3 sliders
ax_x = plt.axes([0.15, 0.20, 0.65, 0.03])
ax_y = plt.axes([0.15, 0.13, 0.65, 0.03])
ax_z = plt.axes([0.15, 0.06, 0.65, 0.03])

slider_x = Slider(ax_x, 'Sagittal', 0, data.shape[0]-1, valinit=slice_x, valstep=1)
slider_y = Slider(ax_y, 'Coronal', 0, data.shape[1]-1, valinit=slice_y, valstep=1)
slider_z = Slider(ax_z, 'Axial', 0, data.shape[2]-1, valinit=slice_z, valstep=1)

# Step 5: Update images when sliders move
def update(val):
    img_x.set_data(data[int(slider_x.val), :, :])
    img_y.set_data(data[:, int(slider_y.val), :])
    img_z.set_data(data[:, :, int(slider_z.val)])
    fig.canvas.draw_idle()

slider_x.on_changed(update)
slider_y.on_changed(update)
slider_z.on_changed(update)

plt.show()
print("Done!")