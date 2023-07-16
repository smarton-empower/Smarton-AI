import pcbnew


def get_fp_by_ref(fps, ref):
    for fp in fps:
        if fp.GetReference() == ref:
            return fp
    return None


class basic_operations(pcbnew.ActionPlugin):
    """
    【TODO】SOME NECESSARY INTRODUCTION
    """

    def defaults(self):
        self.name = "change"
        self.category = "ch"
        self.description = "Basic Operations"

    def Run(self):
        # load board
        board = pcbnew.GetBoard()

        # load footprints (e.g. a resistor, a capacitor)
        footprints = board.GetFootprints()

        # sample: rotate one footprint
        fp = get_fp_by_ref(footprints, 'P1')
        rotate_angle = 10
        fp.SetOrientationDegrees(fp.GetOrientationDegrees() + rotate_angle)

        # sample: move one footprint
        fp = get_fp_by_ref(footprints, 'P2')
        new_pos = [fp.GetX() + 10000000, fp.GetY() + 10000000]
        fp.SetPosition(pcbnew.VECTOR2I(*new_pos))

        # sample: flip one footprint
        fp = get_fp_by_ref(footprints, 'P3')
        fp.Flip(fp.GetPosition(), True)

        # sample: rotate the selected footprint
        selected_fps = [x for x in footprints if x.IsSelected()]
        for fp in selected_fps:
            fp.SetOrientationDegrees(40)


basic_operations().register()