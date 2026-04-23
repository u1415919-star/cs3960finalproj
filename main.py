import streamlit as st
from graph.campus_graph import load_graph
from graph.dijkstra import dijkstra
from ui.map_view import build_map_figure

st.set_page_config(page_title="Campus Navigator", layout="wide")
st.title("Mock Path Advisor for UofU Campus")

nodes, edges, graph = load_graph()
node_labels = {nid: data["label"] for nid, data in nodes.items()}

# Side bar
with st.sidebar:
    st.header("Find a Route")
    building_ids = [nid for nid, data in nodes.items() if data.get("type") == "building"]

    start = st.selectbox("Start", options=building_ids,
                format_func=lambda x: node_labels[x])
    end   = st.selectbox("End",   options=building_ids,
                     format_func=lambda x: node_labels[x], index=1)
    go    = st.button("Find Shortest Path", use_container_width=True)

# Main map
path, cost = [], 0

if go:
    if start == end:
        st.sidebar.warning("Start and end must be different.")
    else:
        path, cost = dijkstra(graph, start, end)
        if not path:
            st.sidebar.error("No path found between those buildings.")
        else:
            st.sidebar.success("Path found!")

fig = build_map_figure(nodes, edges, path)
st.plotly_chart(fig, use_container_width=True, config={"scrollZoom": True})