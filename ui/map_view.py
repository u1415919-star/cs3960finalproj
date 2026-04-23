import plotly.graph_objects as go
from PIL import Image

def build_map_figure(nodes, edges, path=[]):
    img = Image.open("assets/myclassmap.png")
    img_width, img_height = img.size

    fig = go.Figure()

    # Background map image
    fig.add_layout_image(
        dict(
            source=img,
            xref="x", yref="y",
            x=0, y=0,
            sizex=img_width,
            sizey=img_height,
            sizing="stretch",
            layer="below"
        )
    )

    # Build set of path edges for quick lookup
    path_edges = set()
    for i in range(len(path) - 1):
        path_edges.add((path[i], path[i+1]))
        path_edges.add((path[i+1], path[i]))

    #Draw edges 
    for edge in edges:
        a, b = edge["from"], edge["to"]
        x0, y0 = nodes[a]["x"], nodes[a]["y"]
        x1, y1 = nodes[b]["x"], nodes[b]["y"]
        is_path = (a, b) in path_edges
    
        if not is_path:
            continue

        fig.add_trace(go.Scatter(
            x=[x0, x1, None],
            y=[-y0, -y1, None],
            mode="lines",
            line=dict(
                color="#f97316" if is_path else "#94a3b8",
                width=4 if is_path else 1.5,
            ),
            hoverinfo="skip",
            showlegend=False
        ))

    # Draw nodes
    for node_id, data in nodes.items():
        on_path = node_id in path
        is_waypoint = data.get("type") == "waypoint"

        if is_waypoint and not on_path:
            continue

        fig.add_trace(go.Scatter(
            x=[data["x"]],
            y=[-data["y"]],
            mode="markers",
            marker=dict(
                size=12 if on_path else 8,
                color="#f97316" if on_path else "#3b82f6",
                line=dict(width=2, color="white")
            ),
            text=data["label"],
            textposition="top center",
            textfont=dict(size=10, color="white"),
            hovertemplate=f"<b>{data['label']}</b><extra></extra>",
            showlegend=False
        ))

    # Layout 
    fig.update_layout(
        xaxis=dict(range=[0, img_width], visible=False),
        yaxis=dict(range=[-img_height, 0], visible=False, scaleanchor="x"),
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor="#1e293b",
        plot_bgcolor="#1e293b",
        dragmode="pan",
        height=500
    )

    return fig