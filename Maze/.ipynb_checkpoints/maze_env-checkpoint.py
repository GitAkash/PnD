# -*- coding: utf-8 -*-
"""
j.s.kanger Oct 2023
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib; matplotlib.use("TkAgg")

"""
Module for creating and plotting a maze.
functions:

    def make(size=15, render=True, seed=None)
        
        Creates a maze environment
        
        size: integer: gives the dimension of the square maze. size must be uneven and > 5.
        render: Boolean: if True, the maze is rendered in a matplotlib figure
        seed: integer: seeds the random generator. 
        
        Returns the environment
    

"""

MARKERS = ('^', '>', 'v', '<')


def _plot_maze(maze, loc, direction=None, path=None, fig=None, **kwargs):
    """
    Plots the maze a_maze on a grid and plots the path as a blue line on top
    of it begin- and endpoint are indicated with red and green dot respectively
    
    maze:   square 2D numpy array of Booleans.
    loc:    tuple of 2 integers with the row and column index of the mouse
            location.
    path:   2D numpy array of N rows and 2 columns, in which each row
            contains the row and column index of consecutive positions in
            the maze that together form the way out of the maze.
    """

    # creat a new figure with adapted settings
    if fig == None:
        fig, ax = plt.subplots(**kwargs)
        ax = fig.gca()
        plt.cla()
        ax.spines['top'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.xaxis.set_label_position('top')
        ax.tick_params(labeltop=True)
        ax.tick_params(top=True)
        ax.tick_params(labelbottom=False)
        ax.tick_params(bottom=False)

        # plotting of the maze
        plt.imshow(maze, aspect='equal', cmap='Greens')
        N = len(maze)
        plt.xlim([-0.5, N - 0.5])  # skip half of the boundaries
        plt.ylim([-0.5, N - 0.5])  # idem
        plt.xlabel('Column number')
        plt.ylabel('Row number')
        plt.gca().invert_yaxis()  # invert to start at top to get row number right
        ax.plot(loc[1], loc[0], marker=MARKERS[direction])

    # plot start location if provided
    if loc is not None:
        # Note x and y are flipped to match row and column of the maze.
        fig.gca().lines[0].set_data(loc[1], loc[0])
        fig.gca().lines[0].set_marker(MARKERS[direction])

    # if a path is provided, plot it as an overlay
    if path is not None:
        # Note x and y are flipped to match row and column of the maze.
        plt.plot(path[:, 1], path[:, 0], 'xkcd:bright blue', linewidth=2)

    fig.canvas.draw()
    fig.canvas.flush_events()
    return fig


def _make_maze(n, seed, perfect=True):
    """
    Function that generates a maze based on recursive division algorithm
    The maze starts at a point closest to the center that is no wall
    The maze has an exit(s) on one of the four borders

    Arguments: n    Integer specifying the maze size
                    The maze is square with dimension n x n,
                    n  must be uneven and at least 5!

    Returns: maze      The maze is defined as a 2D numpy array of booleans,
                    where walls are indicated with True (1) value and open
                    space with a False (0) value.
            start   Tuple of two integers specifying the row and column
                    indices of the starting location in the maze.

    """

    # check for non-valid values of n
    if np.mod(n, 2) == 0:
        raise ValueError('dimension of maze must be uneven')
    if n <= 5:
        raise ValueError('dimension of maze must be larger than 5')

    # initialize parameters
    WALL = True
    rng = np.random.default_rng(seed)

    def make_exit(maze):
        """
        Make a hole in the surrounding wall of maze A at random but only where
        there is a path behind it and where there is currently no hole.
        Changes the maze in place.
        """
        N = len(maze)
        valid = False

        # keep trying to make exit until matching column/row is found with path
        while not valid:
            side = rng.integers(low=0, high=4)  # pick a side
            index = rng.integers(low=0, high=N - 1) + 1  # pick an index
            if side == 0:  # left
                wall = (index, 0)
                path = (index, 1)

            elif side == 1:  # right
                wall = (index, N - 1)
                path = (index, N - 2)

            elif side == 2:  # top
                wall = (0, index)
                path = (1, index)

            elif side == 3:  # bottom
                wall = (N - 1, index)
                path = (N - 2, index)

            if maze[path] != WALL and maze[wall] == WALL:
                maze[wall] = not WALL
                valid = True

        return

    def split_maze(maze):
        """
        Recursive subfunction that splits the maze in two random sections
        and opens the wall in one place
        walls are always placed on even indices of the matrix and
        openings always on the uneven indices.
        """

        ydim, xdim = maze.shape

        # if maze is too small to split: return
        if (xdim < 3) or (ydim < 3):
            return

        # if xdim larger than ydim split vertical and split submazes
        if xdim >= ydim:
            xsplit = 1 + 2 * rng.integers(low=0, high=int((xdim - 1) / 2))
            pos = 2 * rng.integers(low=0, high=int((ydim + 1) / 2))
            maze[:, xsplit] = True
            maze[pos, xsplit] = False
            split_maze(maze[:, 0:xsplit])
            split_maze(maze[:, xsplit + 1:xdim])

        # else split horizontal and split submazes
        else:
            ysplit = 1 + 2 * rng.integers(low=0, high=int((ydim - 1) / 2))
            pos = 2 * rng.integers(low=0, high=int((xdim + 1) / 2))
            maze[ysplit, :] = True
            maze[ysplit, pos] = False
            split_maze(maze[0:ysplit, :])
            split_maze(maze[ysplit + 1:ydim, :])

        return

    def delete_walls(maze, epsilon):
        """remove walls at random with a probability of epsilon"""
        ydim, xdim = maze.shape

        for r in range(1, ydim - 1):
            for c in range(1, xdim - 1):
                if (maze[r, c] == WALL) and (maze[r - 1, c] != WALL and maze[r + 1, c] != WALL) or (
                        maze[r, c - 1] != WALL and maze[r, c + 1] != WALL):
                    if rng.uniform() < epsilon:
                        maze[r, c] = not WALL

    # make an empty maze surrounded by walls of dimensions n x n
    maze = np.ones((n, n), dtype=bool)
    maze[1:-1, 1:-1] = np.zeros((n - 2, n - 2), dtype=bool)

    # create walls in the empty maze
    split_maze(maze[1:-1, 1:-1])

    # determine starting point default is center if this is a wall choose from
    # surrounding cells
    c = round((n - 1) / 2)  # index of center row and column
    if not maze[c, c]:
        start = (c, c)
    else:
        free_locations = list(zip(*np.where(maze[c - 1:c + 2, c - 1:c + 2] == False)))
        free_locations = [(loc[0] + c - 1, loc[1] + c - 1) for loc in free_locations]  # correct for offset
        choice = rng.integers(low=0, high=len(free_locations))
        start = free_locations[choice]

    # remove at random some walls to create loops if required
    if not perfect:
        delete_walls(maze, epsilon=0.1)

    # create the exits to the maze at random sides
    make_exit(maze)

    return maze, np.array(start)


def make(size=15, seed=None, perfect=True):
    """
    creates and returns a MazeEnv class to interact with a maze environment
    size: integer: size of the maze. size must be uneven and larger than 5.
    seed: integer: By setting a value to seed you can reproduce the same maze again 
    perfect: Boolean: If True generates a perfect maze (no loops, one solution).
    """

    # intialization
    _maze, _start_loc = _make_maze(size, seed, perfect)
    _bounds = (0, size - 1)
    _loc = _start_loc
    _action = 0  # facing north
    _delta = np.array([[-1, 0], [0, 1], [1, 0], [0, -1]])
    _fig = None

    class MazeEnv():
        """
        An environment for navigating a maze.

        This class provides methods to interact with a maze environment,
        including moving through the maze, rendering it, and resetting the state.

        User relevant methods:
        - action_space(): Get the available actions for the current state.
        - step(action): Take a step in the environment with the given action.
        - render(path=None, newfig=False): Render the maze, optionally showing a path.
        - reset(): Reset the environment to its initial state.

        """

        def __init__(self):
            pass

        def _done(self):
            """returns True if the current location is an exit"""
            return _loc[0] in _bounds or _loc[1] in _bounds

        def _getindex(self, action):
            """returns the index in maze given the value of action"""
            return _loc + _delta[action]

        def _state(self):
            """returns the current gamestate"""
            return tuple(_loc), self._done()

        def action_space(self):
            """
            returns a list of available actions in the current state
            """
            space = [action for action in range(4) if not _maze[tuple(self._getindex(action))]]
            return space

        def step(self, action):
            """
            perform action and return new state
            
            Arguments:
            action: integer 0 (up), 1 (right), 2 (down), or 3 (left)
            
            Returns:
            state: tuple, boolean: 
                tuple gives location in maze as (rownr, colnr)
                boolean is True when location is exit and False otherwise
            
            """
            nonlocal _loc, _action
            _action = action
            _new_loc = self._getindex(action)
            if not _maze[tuple(_new_loc)]:
                _loc = _new_loc
            return self._state()

        def render(self, path=None, newfig=False):
            """
            renders the maze in a matplotlib figure
            path: 2D ndarray of locations: path that is plotted as an overlay
            newfig: Boolean: if True a newfigure is created, if False the current figure is updated
            """
            nonlocal _fig
            if _fig is None or newfig:
                _fig = _plot_maze(_maze, _loc, _action)
            _plot_maze(_maze, _loc, _action, path=path, fig=_fig)
            return None

        def reset(self):
            """resets the gamestate to the intial position and returns the gamestate"""
            nonlocal _loc, _action
            _loc = _start_loc
            _action = 0
            return self._state()

    return MazeEnv()