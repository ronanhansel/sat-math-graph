import numpy as np

import matplotlib.pyplot as plt

def plot_linear_function(function: str, point=None, x_step=1, y_step=1, max_x=10, max_y=10, n_max_x=10, n_max_y=10, ):
    # Create a range of x values
    x = np.linspace(-10, 10, 400)
    # Calculate the corresponding y values

    y = eval("lambda x: " + function)(x)

    # Create the plot
    fig, ax = plt.subplots()

    # Plot the function
    ax.plot(x, y)

    # Draw the x and y axes
    ax.axhline(0, color='black',linewidth=0.5)
    ax.axvline(0, color='black',linewidth=0.5)

    # Add label 'x' at the end of the x-axis line
    ax.text(10, 0.5, 'x', fontsize=12, ha='left', va='center', fontname='Times New Roman', fontstyle='italic')
    ax.text(0.5, 10, 'y', fontsize=12, ha='left', va='center', fontname='Times New Roman', fontstyle='italic')

    # Set the grid with custom steps
    ax.set_xticks(np.arange(-10, 11, x_step))
    ax.set_yticks(np.arange(-10, 11, y_step))
    ax.grid(True, which='both', color='black', linestyle='-', linewidth=0.5)

    # Hide the right and top spines (side bars)
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # Move bottom and left spines to zero position
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    if point:
        # Draw a point
        x_val, y_val = point
        ax.plot(x_val, y_val, 'o')  # 'ro' means red color, circle marker

    # get width and height of axes object to compute 
    # matching arrowhead length and width
    dps = fig.dpi_scale_trans.inverted()
    bbox = ax.get_window_extent().transformed(dps)
    width, height = bbox.width, bbox.height
    
    # manual arrowhead width and length
    hw = 0.4
    hl = 0.5
    lw = 1. # axis line width
    ohg = 0.3 # arrow overhang
    
    # compute matching arrowhead length and width
    yhw = hw/(max_y-n_max_y + 0.1)*(max_x-n_max_x + 0.1)* height/width 
    yhl = hl/(max_x-n_max_x + 0.1)*(max_y-n_max_y + 0.1)* width/height
    
    # draw x and y axis
    ax.arrow(n_max_x, 0, max_x-n_max_x + 0.1, 0., fc='k', ec='k', lw = lw, 
            head_width=hw, head_length=hl, overhang = ohg, 
            length_includes_head= True, clip_on = False) 
    
    ax.arrow(0, n_max_y, 0., max_y-n_max_y + 0.1, fc='k', ec='k', lw = lw, 
            head_width=yhw, head_length=yhl, overhang = ohg, 
            length_includes_head= True, clip_on = False) 
    
    # Set the limits for the x and y axes
    ax.set_xlim(-n_max_x, max_x)
    ax.set_ylim(-n_max_y, max_y)

    # Set the line color to black
    for line in ax.get_lines():
        line.set_color('black')

    # Show the plot
    plt.show()

if __name__ == "__main__":
    # Input the slope and intercept of the linear function
    x_step = 2
    y_step = 2
    max_x = 10
    max_y = 10
    n_max_x = 10
    n_max_y = 10
    f = input("Enter the function: y=")

    plot_linear_function(function=f, point=None, x_step=x_step, y_step=y_step, max_x=max_x, max_y=max_y, n_max_x=n_max_x, n_max_y=n_max_y)
    # plot_linear_function(function='np.exp(x)', point=None, x_step=x_step, y_step=y_step, max_x=max_x, max_y=max_y, n_max_x=n_max_x, n_max_y=n_max_y)