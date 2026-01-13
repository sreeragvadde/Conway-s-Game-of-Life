from matplotlib import pyplot as plt


def view_grid(grid: list, frame_delay: float, step_number: int) -> None:
    """
    shows an image of the current state of the grid
    parameters:
        grid - list-of-lists representing the current grid. Inner lists use 0s to represent dead cells, and 1s to represent live ones
        frame_delay - the program will pause for this many seconds after displaying the image. 0.1s gives a pretty good animation effect
        step_number - the step number of the supplied grid (will be displayed above the image)
    """

    # check that the grid supplied is not empty
    if len(grid) == 0:
        raise Exception("grid is empty")

    # check that all rows contain the same number of cells
    row_lengths = set([len(row) for row in grid])
    if len(row_lengths) != 1:
        raise Exception(f"not all grid rows are the same length. Found lengths: {row_lengths}")

    # check that all rows contain only 0s and 1s
    if not all([set(row) <= {0, 1} for row in grid]):
        raise Exception("only 0 and 1 are allowed in grid")

    # plot the grid
    plt.cla()
    plt.imshow(grid)
    plt.title(f'step {step_number}')
    plt.pause(frame_delay)

def main(input_filename: str, output_filename: str) -> None:
    """
    main function
    parameters:
        input_filename: file to read the starting configuration from
        output_filename: file to write the ending configuration (after 100 steps) to
        display: if True, the program should display the grid steps (using the provided view_grid function)
                 if False, the program should not display the grid steps.
    """
    grid=read(input_filename)
    final_grid=display_steps(grid) 
    outputfile_name(output_filename,final_grid)   
  
def read(input_filename: str) ->list:
    """
    Takes input of txt file as a List
    """
    file=open(input_filename,"r", encoding="UTF-8")
    lines=file.readlines()
    char=[]
    grid=[]
    for row in lines[1:-1]:
         for word in row:
            if word=="█":
                 char.append(1)
            elif word==" ":
                char.append(0)
         grid.append(char)
         char=[]
    file.close()
    return grid

def display_steps(grid:list) ->list:
    """
    Displays the steps of the cells
    """
    i=1
    while i<=100:
        grid=alive_or_dead(grid)
        view_grid(grid,0.1,i)
        i=i+1
    return grid

def alive_or_dead(grid:list) ->list:
    """
    Checks if the cell is alive or dead
    """
    row_list=[]
    final_grid=[]
    for i in range(len(grid)):
        row=grid[i]      
        for a in range(len(row)):
            cell=row[a]
            alive_near=0
            if a+1<len(row):
                if row[a+1]==1:
                    alive_near+=1
            if a-1>=0:
                if row[a-1]==1:
                    alive_near+=1
            if i+1<len(grid):
                if grid[i+1][a]==1:
                    alive_near+=1
                if a+1<len(row):
                    if grid[i+1][a+1]==1:
                        alive_near+=1
                if a-1>=0:
                    if grid[i+1][a-1]==1:
                        alive_near+=1
            if i-1>=0:
                if grid[i-1][a]==1:
                    alive_near+=1
                if a+1<len(row):
                    if grid[i-1][a+1]==1:
                        alive_near+=1
                if a-1>=0:
                    if grid[i-1][a-1]==1:
                        alive_near+=1
            if cell==0 and alive_near==3:
                row_list.append(1)
            elif cell==1 and (alive_near==3 or alive_near==2):
                row_list.append(1)
            else:
                row_list.append(0)
        final_grid.append(row_list)
        row_list=[]
    return final_grid

def outputfile_name(output_filename: str, final_grid: list) ->None:
    """
    Converts the output list to a txt file of your choice
    """
    file=open(output_filename,"w",encoding="UTF-8")
    for row in final_grid:
        for cell in row:
            if cell==1:
                file.write("█") 
            else:
                file.write(" ")
        file.write("\n")
    file.close()

# main("data/input/a.txt","data/output/a_answer.txt")
# main("data/input/b.txt","data/output/b_answer.txt")
# main("data/input/sheldon.txt","data/output/sheldon_answer.txt")

main("data/input/c.txt","data/output/c_answer.txt")
