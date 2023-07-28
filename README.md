

Working on the conversions needed to use Phoenix as an event display

Convert from XML to TGeo objects using this (working inside of `infnpd/mucoll-ilc-framework:1.7-almalinux9`):

```
geoConverter -compact2tgeo -input detector-simulation/geometries/MuColl_10TeV_v0A//MuColl_10TeV_v0A.xml -output MuColl_10TeV_v0A.root
```

https://github.com/HSF/phoenix/blob/main/guides/developers/convert-gdml-to-gltf.md#concert-root-to-gltf

