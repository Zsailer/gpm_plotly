import igraph
import plotly
from plotly.graph_objs import *

import matplotlib
import numpy as np

def mpl_to_plotly_colorscale(cmap_name):
    """Matplotlib colormap to plotly colormap.

    Taken from this page:
    https://plot.ly/python/matplotlib-colorscales/
    """
    cmap = matplotlib.cm.get_cmap(cmap_name)

    cmap_rgb = []
    norm = matplotlib.colors.Normalize(vmin=0, vmax=255)
    for i in range(0, 255):
       k = matplotlib.colors.colorConverter.to_rgb(cmap(norm(i)))
       cmap_rgb.append(k)

    h = 1.0/(255-1)
    pl_colorscale = []

    for k in range(255):
        C = list(map(np.uint8, np.array(cmap(k*h)[:3])*255))
        pl_colorscale.append([k*h, 'rgb'+str((C[0], C[1], C[2]))])

    return pl_colorscale

def draw(GenotypePhenotypeMap, edges,
    fig_height=500,
    fig_width=900,
    node_size=10,
    node_opacity=1,
    edge_opacity=1,
    edge_colors="rgb(125,125,125)",
    edge_widths=1,
    colorscale="plasma"):
    """
    """
    gpm = GenotypePhenotypeMap

    # Calculate the force directed positions of nodes in 3d.
    iG = igraph.Graph(edges, directed=False)
    pos = iG.layout("kk", dim=3)

    # Get node positions
    xnode = [pos[i][0] for i in range(gpm.n)]
    ynode = [pos[i][1] for i in range(gpm.n)]
    znode = [pos[i][2] for i in range(gpm.n)]

    # Get edge positions
    xedge = [(pos[i][0], pos[j][0]) for i,j in edges]
    yedge = [(pos[i][1], pos[j][1]) for i,j in edges]
    zedge = [(pos[i][2], pos[j][2]) for i,j in edges]

    # Styles
    labels = gpm.genotypes
    colors = gpm.phenotypes

    # Create nodes for visualization
    Nodes = Scatter3d(x=xnode, y=ynode, z=znode,
        mode="markers",
        name="genotypes",
        marker=Marker(symbol="dot",
            size=node_size,
            color=colors,
            opacity=node_opacity,
            colorscale=mpl_to_plotly_colorscale(colorscale)),
        text=labels,
        hoverinfo="text")

    # Create edges for visualization
    Edges = []
    for i in range(len(edges)):
        Edge = Scatter3d(x=xedge[i], y=yedge[i], z=zedge[i],
            opacity=edge_opacity,
            mode="lines",
            line=Line(color=edge_colors,width=edge_widths))
        Edges.append(Edge)

    # Prepare axis
    Axis = dict(showbackground=False,
        showline=False,
        zeroline=False,
        showgrid=False,
        showticklabels=False,
        title="",
        showspikes=False)

    # Prepare Layout
    Frame = Layout(width=fig_width,
        height=fig_height,
        showlegend=False,
        scene=Scene(xaxis=XAxis(Axis), yaxis=YAxis(Axis), zaxis=ZAxis(Axis)),
        hovermode="closest")

    # Combine Data and prepare for graph
    Dat = Data(Edges + [Nodes])
    Fig = Figure(data=Dat, layout=Frame)

    return Fig
