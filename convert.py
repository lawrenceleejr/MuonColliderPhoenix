

import pyg4ometry

excludeList = [
"BeampipeOuter",
# "module",
"Support",
"InterlinkTube",
"Cable",
"Shell",
"layer0_supp",
"layer1_supp",
"layer2_supp",
"layer4_supp",
"layer6_supp",
]

for i in range(20)[1:]:
    excludeList.append(f"component{i}_{i}")

def recurseThroughTree(vol):
    for i in vol.daughterVolumes:

        if any([x in i.name for x in excludeList]):
            # print(f"removing {i.name}")
            i.visOptions.alpha = 0

        i.visOptions.color = [1.0,1,1]

        if i.visOptions.alpha>0:
            i.visOptions.alpha = 1.0
        try:
            if i.logicalVolume.material.name=="Air":
                # print(i.name)
                i.visOptions.visible = False
                i.visOptions.alpha = 0

                # i.scale = 0
                # i.extent = 0
        except:
            pass
        recurseThroughTree(i.logicalVolume)


colors = {
            "Nozzle":[0.8,0.8,0.8,1.0],
            "Yoke":[0.9,0.5,0.5,1.0],
            "HCal":[0.5,0.9,0.5,1.0],
            "ECal":[0.5,0.5,0.9,1.0],
            "InnerTracker":[0.5,0.9,0.9,1.0],
            "OuterTracker":[0.9,0.9,0.5,1.0],
}

for thing in [
            # "Nozzle",
            # "Yoke",
            # "HCal",
            # "ECal",
            "InnerTracker",
            # "OuterTracker",
            ]:

    print(thing)
    r = pyg4ometry.gdml.Reader(f"MuColl_10TeV_v0A_{thing}.gdml")
    l = r.getRegistry().getWorldVolume()

    # print(l)
    import pyg4ometry.misc as _misc
    import pyg4ometry.geant4 as _g4
    reg = _g4.Registry()
    # clipFW = 60
    # clipBox = _g4.solid.Box("clipper", clipFW, clipFW, clipFW, reg, "m")
    # clipBoxes = _misc.NestedBoxes("clipper",clipFW, clipFW, clipFW, reg, "m", 0,0,0, l.depth())

    # l.changeSolidAndTrimGeometry(clipBox,(0,0,0),(0,0,0))
    # l.clipGeometry(clipBoxes,(0,0,0),(30,0,0))

    print("Editing input GDML")
    recurseThroughTree(l)

    v = pyg4ometry.visualisation.VtkViewerColouredNew()
    print("adding LV")
    v.addLogicalVolume(l)
    print("removing invisible elements")
    v.removeInvisible()
    v.scaleScene(0.01)
    # v.addClipper([0,0,0],[1,0,0],True)
    # v.addCutter("bisect",[0,0,0],[1,0,0])

    v.buildPipelinesAppend()
    # v.addClipperWidget()

    v.exportGLTFScene(f"{thing}.gltf", color=colors[thing])



