

Working on the conversions needed to use Phoenix as an event display

Convert from XML to TGeo objects using this (working inside of `infnpd/mucoll-ilc-framework:1.7-almalinux9`):

```
docker run --rm -ti -v $PWD:$PWD -w $PWD -e DISPLAY=$DISPLAY -v $XSOCK:$XSOCK -v $XAUTH:$XAUTH   -e XAUTHORITY=$XAUTH --net host infnpd/mucoll-ilc-framework:1.7-almalinux9
```

```
geoConverter -compact2gdml -input detector-simulation/geometries/MuColl_10TeV_v0A//MuColl_10TeV_v0A.xml -output MuColl_10TeV_v0A_Yoke.gdml

```

https://github.com/HSF/phoenix/blob/main/guides/developers/convert-gdml-to-gltf.md#concert-root-to-gltf

