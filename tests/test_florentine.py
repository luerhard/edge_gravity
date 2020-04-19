import networkx as nx
from edge_gravity import edge_gravity


def test_florentine_k_15():
    florentine_family = nx.generators.social.florentine_families_graph()

    new_g = nx.DiGraph()
    for node in florentine_family.nodes():
        new_g.add_node(node)

    for u, v in florentine_family.edges():
        new_g.add_edge(u, v)
        new_g.add_edge(v, u)

    florentine_family = new_g

    kstar_found, results = edge_gravity(florentine_family, k=15)
    results = results.most_common(40)

    assert kstar_found == False

    exp_results = set([
        (("Bischeri", "Guadagni"), 727),
        (("Guadagni", "Bischeri"), 717),
        (("Strozzi", "Ridolfi"), 677),
        (("Ridolfi", "Strozzi"), 676),
        (("Barbadori", "Castellani"), 573),
        (("Castellani", "Barbadori"), 562),
        (("Bischeri", "Peruzzi"), 543),
        (("Medici", "Barbadori"), 526),
        (("Peruzzi", "Bischeri"), 525),
        (("Guadagni", "Tornabuoni"), 518),
        (("Barbadori", "Medici"), 515),
        (("Tornabuoni", "Guadagni"), 506),
        (("Tornabuoni", "Ridolfi"), 486),
        (("Ridolfi", "Tornabuoni"), 485),
        (("Castellani", "Peruzzi"), 482),
        (("Peruzzi", "Castellani"), 472),
        (("Castellani", "Strozzi"), 471),
        (("Strozzi", "Castellani"), 470),
        (("Tornabuoni", "Medici"), 455),
        (("Medici", "Tornabuoni"), 444),
        (("Strozzi", "Bischeri"), 442),
        (("Peruzzi", "Strozzi"), 441),
        (("Albizzi", "Guadagni"), 436),
        (("Guadagni", "Albizzi"), 434),
        (("Ridolfi", "Medici"), 416),
        (("Bischeri", "Strozzi"), 414),
        (("Medici", "Ridolfi"), 414),
        (("Strozzi", "Peruzzi"), 413),
        (("Medici", "Albizzi"), 398),
        (("Albizzi", "Medici"), 396),
        (("Medici", "Salviati"), 334),
        (("Salviati", "Medici"), 334),
        (("Albizzi", "Ginori"), 196),
        (("Guadagni", "Lamberteschi"), 196),
        (("Lamberteschi", "Guadagni"), 196),
        (("Ginori", "Albizzi"), 196),
        (("Medici", "Acciaiuoli"), 168),
        (("Salviati", "Pazzi"), 168),
        (("Acciaiuoli", "Medici"), 168),
        (("Pazzi", "Salviati"), 168),
    ])

    assert set(results) == exp_results
