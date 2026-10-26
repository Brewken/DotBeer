# Equipment

Groups together all the vessels in a set of brewing equipment.  Note that, in some set-ups, one vessel serves multiple purposes -- eg mash tun and kettle may be the same physical vessel -- but there are nonetheless individual entries here for each "purpose".

<strong>Equipment</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| name | ✅ | string |  |
| kettle | ✅ | [BoilKettle](#boilkettle) | Boil Kettle |
| local_id |  | [DotBeer::LocalId](./DotBeer.md#localid) | The "local ID" that allows other objects in this file (eg recipes) to refer to this set of equipment. |
| folder_path |  | [DotBeer::FolderPath](./DotBeer.md#folderpath) | The suggested slash-delimited subfolder path in which to store this Equipment object. |
| hlt |  | [HotSideVessel](#hotsidevessel) | Hot Liquor Tank |
| mash_tun |  | [MashTun](#mashtun) | Mash Tun |
| lauter_tun |  | [HotSideVessel](#hotsidevessel) | Lauter Tun |
| fermentation_vessel |  | [Vessel](#vessel) | Fermentation Vessel |
| aging_vessel |  | [Vessel](#vessel) | Aging Vessel |
| packaging_vessel |  | [Vessel](#vessel) | Packaging Vessel |


---

# Component Types

## Vessel

An individual vessel (eg mash tun, boil kettle) that forms part of brewing equipment.

<strong>Vessel</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| max_volume | ✅ | [Measurement::Volume](./Measurement.md#volume) | Maximum usable capacity of the vessel. |
| loss | ✅ | [Measurement::Volume](./Measurement.md#volume) | Volume left behind (dead space, trub, chiller) when transferring out of this vessel |
| vessel_type |  | string | Free text type of the vessel, such as its material or model. |
| notes |  | string |  |

## HotSideVessel

A vessel used for the hot-side of brewing.

<strong>HotSideVessel</strong> is a JSON object with all properties from [Vessel](#vessel) as well as these additional ones:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| weight |  | [Measurement::Mass](./Measurement.md#mass) | The weight of the piece of equipment, especially important for when the mash tun is not preheated. |
| specific_heat_capacity |  | [Measurement::SpecificHeatCapacity](./Measurement.md#specificheatcapacity) | The specific heat capacity of the piece of equipment, especially important for when the mash tun is not preheated. |

## MashTun

A hot-side vessel used for the mash.

<strong>MashTun</strong> is a JSON object with all properties from [HotSideVessel](#hotsidevessel) as well as these additional ones:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| grain_absorption_rate |  | [Measurement::VolumePerMass](./Measurement.md#volumepermass) | The apparent volume absorbed by grain, typical values are 0.125 gal/lb (1.04 l/kg) for a mash tun, 0.08 gal/lb (0.66 l/kg) for BIAB. |
| foundation_volume |  | [Measurement::Volume](./Measurement.md#volume) | Volume of liquid in the mash tun that is outside the grain bed -- typically below a false bottom, screen or malt pipe -- and so is needed in addition to the water that wets the grain, but which, unlike `loss`, drains out with the wort and is recovered (eg into the boil).  Typical of all-in-one systems: eg 3.5 l for a Grainfather G30.<br /><br />Relationship to other fields:<br>• **`loss`** is the volume that never leaves the vessel (eg below the outlet); `foundation_volume` is the volume that does leave it.  No volume is counted in both, so, eg, for a cooler with a false bottom and an outlet above the floor, the volume below the outlet is `loss` and the volume between the outlet and the false bottom is `foundation_volume`.<br>• **`max_volume`** is the vessel's total usable capacity, so it includes both `foundation_volume` and `loss`.  Thus `foundation_volume` plus `loss` must be less than `max_volume`, and the room left for the mash itself is `max_volume` minus both.<br>• **`grain_absorption_rate`** is separate: it covers liquid retained by the grain, not by the vessel.<br /><br />Using it: strike water = (grain mass × mash thickness) + `foundation_volume` + `loss`, where mash thickness is the ratio of water to grain *in the grain bed*.  `foundation_volume` is not subtracted from the wort collected, whereas `loss` is.  If absent, treat it as 0, which is also the right value where there is no separate space below the grain (eg brew-in-a-bag with no false bottom). |

## BoilKettle

A hot-side vessel used for the boil.

<strong>BoilKettle</strong> is a JSON object with all properties from [HotSideVessel](#hotsidevessel) as well as these additional ones:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| boil_rate_per_hour |  | [Measurement::Volume](./Measurement.md#volume) | The volume boiled off during 1 hour, measured before and after at room temperature. |
| drain_rate_per_minute |  | [Measurement::Volume](./Measurement.md#volume) | The volume that leaves the kettle, especially important for non-immersion chillers that cool the wort as it leaves the kettle. |
| internal_diameter |  | [Measurement::Length](./Measurement.md#length) | With opening_diameter, allows calculation of IBU by John-Paul Hosom's mIBU formula |
| opening_diameter |  | [Measurement::Length](./Measurement.md#length) | With internal_diameter, allows calculation of IBU by John-Paul Hosom's mIBU formula |



---

Documentation generated from the [dotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) (v1.0.0) on 2026-10-26 at 10:19:49+0100.
