
digraph G {
  rankdir=TB; bgcolor="white"; node [shape=box, style="rounded,filled", fontname="Arial", fontsize=10]; edge [fontname="Arial", fontsize=9];
  ui [fillcolor="#e8f0fe", label="Capa de Interfaz\nMenú de consola"];
  logic [fillcolor="#e6ffed", label="Capa Lógica\nValidaciones, reportes, alertas"];
  model [fillcolor="#fff3cd", label="Modelo de Datos\nClase Producto"];
  storage [fillcolor="#fde2e2", label="Persistencia\nArchivo inventario.json"];
  ui -> logic; logic -> model; logic -> storage; storage -> logic;
}
