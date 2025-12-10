'''
import io
import uuid
from django.core.files.base import ContentFile
import matplotlib.pyplot as plt

def save_matplotlib_figure(fig, visualization):
    # Create an io stream in memory
    buffer = io.BytesIO()
    # Write the figure to the buffer stream as a png with 150 dots per inch, cropping whitespace around the figure
    fig.savefig(buffer, format='png', dpi=150, bbox_inches='tight')
    # Reset the buffer's position to the beginning so we can read its contents
    buffer.seek(0)

    # Save the buffer to the model entry's image field
    visualization.image_file.save(
        f"viz_{uuid.uuid4().hex}.png",
        ContentFile(buffer.read()),
        save=True
    )

    plt.close(fig)
    return visualization
'''

import io
import uuid
from django.core.files.base import ContentFile


def save_plotly_figure(fig, visualization):
    # Create an io stream in memory
    buffer = io.BytesIO()

    # Write the figure to the buffer
    fig.write_image(buffer, format="png", scale=2)
    # Reset the buffer's position to the beginning so we can read its contents
    buffer.seek(0)

    # Store the buffer in the model entry's image field
    visualization.image_file.save(
        f"viz_{uuid.uuid4().hex}.png",
        ContentFile(buffer.read()),
        save=False
    )

    # Store the plotly figure's json in the model entry
    fig_json = fig.to_json()
    visualization.plotly_json = fig_json

    visualization.save()

    return visualization