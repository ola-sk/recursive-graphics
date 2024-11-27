import numpy as np

def draw_sine_wave_segment(canvas, x, y, end_x, end_y, line_len, wave_amp, fill, width=1):
    # Calculate the angle of rotation
    angle = np.arctan2(end_y - y, end_x - x)

    period_scale = 2*np.pi / line_len
    
    # Generate sine wave points
    t = np.linspace(0, line_len, 100)
    sine_wave_x = t
    sine_wave_y = wave_amp*np.sin(period_scale*t)
    
    # Rotate and translate points
    cos_angle = np.cos(angle)
    sin_angle = np.sin(angle)
    transformed_points = []
    for i in range(len(t)):
        new_x = cos_angle * sine_wave_x[i] - sin_angle * sine_wave_y[i] + x
        new_y = sin_angle * sine_wave_x[i] + cos_angle * sine_wave_y[i] + y
        transformed_points.append((new_x, new_y))

    
    
    # Draw the sine wave segment
    for i in range(len(transformed_points) - 1):

        # calculate x and y of the unit vector
        unit_vector_x = transformed_points[i+1][0] - transformed_points[i][0]
        unit_vector_y = transformed_points[i+1][1] - transformed_points[i][1]
        unit_vector_length = np.sqrt(unit_vector_x**2 + unit_vector_y**2)
        unit_vector_x /= unit_vector_length
        unit_vector_y /= unit_vector_length

        canvas.create_line(transformed_points[i][0], transformed_points[i][1],
                           transformed_points[i+1][0]+unit_vector_x*2.5, transformed_points[i+1][1]+unit_vector_y*2.5, width=width, fill=fill)

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb_color):
    return '#{:02x}{:02x}{:02x}'.format(*rgb_color)

def interpolate_color(color1, color2, factor):
    return tuple(int(color1[i] + (color2[i] - color1[i]) * factor) for i in range(3))

def generate_gradient(color1, color2, steps):
    rgb_color1 = hex_to_rgb(color1)
    rgb_color2 = hex_to_rgb(color2)
    gradient = []
    for step in range(steps):
        factor = step / (steps - 1)
        interpolated_color = interpolate_color(rgb_color1, rgb_color2, factor)
        gradient.append(rgb_to_hex(interpolated_color))
    return gradient