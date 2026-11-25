# Equipment

Groups together all the vessels in a set of brewing equipment.  There is an entry for each "role" a vessel can play (hot liquor tank, mash tun, lauter tun, boil kettle, fermentation vessel, aging vessel, packaging vessel).  Only the boil kettle is required.  If a role is absent, it is not played by a separate vessel: there is no transfer to or from such a vessel, and so no loss, and the role (if it happens at all) is played by a neighbouring vessel, as set out in the description of each role.  In particular, if there is no mash tun, the mash happens in the boil kettle, as in single-vessel set-ups such as all-in-one systems (eg Grainfather, BrewZilla) and brew-in-a-bag.

The properties of the mash that relate to the equipment as a whole, rather than to a particular vessel (`grain_absorption_rate` and `foundation_volume`), are at the top level, so that they are in the same place whether the mash happens in a separate mash tun or in the kettle.  Likewise `hop_absorption_rate`, which applies to hops wherever they are left behind (the kettle or the vessel used for dry hopping).

<strong>Equipment</strong> is a JSON object with the following properties:

| Property | Required? | Type | Since | Description |
| -------- | --------- | ---- | ----- | ----------- |
| name | ✅ | string |  |  |
| kettle | ✅ | [BoilKettle](#boilkettle) |  | Boil Kettle.  Always required.  If there is no mash tun, the mash also happens here. |
| local_id |  | [DotBeer::LocalId](./DotBeer.md#localid) |  | The "local ID" that allows other objects in this file (eg recipes) to refer to this set of equipment. |
| folder_path |  | [DotBeer::FolderPath](./DotBeer.md#folderpath) |  | The suggested slash-delimited subfolder path in which to store this Equipment object. |
| default_batch_size |  | [Measurement::Volume](./Measurement.md#volume) |  | The batch size this equipment is normally used for, ie the volume into the fermentation vessel (as for `batch_size` on [Recipe](./Recipe.md#recipe)).  A program may use this as the batch size for a new recipe that uses this equipment.  NB: This is a default, not a limit, and is not the same as the capacity (`max_volume`) of any of the vessels. |
| grain_absorption_rate |  | [Measurement::VolumePerMass](./Measurement.md#volumepermass) |  | The apparent volume absorbed by grain in the mash (whether in the mash tun or, if there is none, the kettle).  Typical values are 0.125 gal/lb (1.04 l/kg) for a conventional mash tun, about 0.8 l/kg (0.1 gal/lb) for an all-in-one system with a malt pipe, and 0.08 gal/lb (0.66 l/kg) for brew-in-a-bag with the bag squeezed.  If absent, nothing is known about it, and a program may assume a typical value. |
| foundation_volume |  | [Measurement::Volume](./Measurement.md#volume) |  | Volume of liquid in the vessel where the mash happens (the mash tun or, if there is none, the kettle) that is outside the grain bed -- typically below a false bottom, screen or malt pipe -- and so is needed in addition to the water that wets the grain, but which drains out with the wort and is recovered (eg into the boil).  Typical of all-in-one systems: eg 3.5 l for a Grainfather G30.<br /><br />Relationship to other fields:<br>• The mash tun's **`loss`** is the volume that never leaves the mash tun (eg below the outlet); `foundation_volume` is the volume that does leave it.  No volume is counted in both, so, eg, for a cooler with a false bottom and an outlet above the floor, the volume below the outlet is `loss` and the volume between the outlet and the false bottom is `foundation_volume`.  (Where the mash happens in the kettle, the kettle's `loss` is about what is left after the boil, so is not relevant here.)<br>• The **`max_volume`** of the vessel where the mash happens is its total usable capacity, so it includes `foundation_volume` (and, for a mash tun, `loss`).  Thus these must add up to less than `max_volume`, and the room left for the mash itself is what remains.<br>• **`grain_absorption_rate`** is separate: it covers liquid retained by the grain, not by the vessel.<br /><br />Using it: strike water = (grain mass × mash thickness) + `foundation_volume` (+ the mash tun's `loss`, if there is a mash tun), where mash thickness is the ratio of water to grain *in the grain bed*.  `foundation_volume` is not subtracted from the wort collected, whereas `loss` is.  If absent, treat it as 0, which is also the right value where there is no separate space below the grain (eg brew-in-a-bag with no false bottom). |
| hop_absorption_rate |  | [HopAbsorptionRate](#hopabsorptionrate) | 1.2.0 | The typical volume of wort or beer that this brewery loses with hop material, per mass of hops (as weighed when added): ie what is retained in or with the hops when the liquid is transferred off them.  This is a net figure that depends on the brewer's process as well as on the hops (eg loose hops versus a hop spider or bag, whether the hops are squeezed or left to drain, whirlpooling and settling time, and how dry hops are separated), so it is best measured -- eg by weighing the wet hop material left behind, or from the shortfall in volume on a hoppy brew.<br /><br />It applies both to hops left in the kettle and to dry hops left in the vessel they were added to.  It is counted in addition to that vessel's `loss`, so `loss` should not also include an allowance for hops.  (Where, eg, loose pellets settle into space that is already counted in the kettle's `loss`, this rate should cover only the extra volume lost because of the hops.)<br /><br />`pellet` is used for hops of form `pellet` and `powder`, and `leaf` for `leaf` and `plug`.  Hop extract is assumed to leave no liquid behind.  No rate is defined for `leaf (wet)`, for which there are no reliable figures; a program should not simply apply the `leaf` rate, which, per mass as weighed, would likely overstate the loss.<br /><br />Reported figures vary widely.  Around 7 ml/g (6.7 floz/oz) for pellets and 5 ml/g (4.8 floz/oz) for leaf hops are reasonable starting points.  (Fully swollen pellets can hold more: 10 - 14 ml/g in tests in water.)  If this field, or one of its rates, is absent, nothing is known about it, and a program may assume a typical value. |
| hlt |  | [HotSideVessel](#hotsidevessel) |  | Hot Liquor Tank.  If absent, water is heated in one of the other vessels (eg the kettle), and no loss is assumed. |
| mash_tun |  | [HotSideVessel](#hotsidevessel) |  | Mash Tun.  If absent, the mash (if any) happens in the boil kettle, as in single-vessel set-ups such as all-in-one systems and brew-in-a-bag.  (For extract brewing, any steeping of grains also happens in the kettle.)  In this case, the kettle's `max_volume`, `weight` and `specific_heat_capacity` apply to the mash, and, because the strike water is heated in the same vessel, there is normally no need to allow for the vessel absorbing heat from the strike water. |
| lauter_tun |  | [HotSideVessel](#hotsidevessel) |  | Lauter Tun.  If absent, lautering happens in the vessel where the mash happens -- the mash tun or, if there is none, the kettle -- and, in the former case, any lautering losses are included in the mash tun's `loss`. |
| fermentation_vessel |  | [Vessel](#vessel) |  | Fermentation Vessel.  If absent, nothing is known about it, and no loss is assumed. |
| aging_vessel |  | [Vessel](#vessel) |  | Aging Vessel.  If absent, there is no transfer to a separate vessel for aging (eg because the beer is aged, if at all, in the fermentation vessel, as with a unitank), and so no loss. |
| packaging_vessel |  | [Vessel](#vessel) |  | Packaging Vessel.  If absent, no loss is assumed in packaging (eg because the beer is served from the vessel it was fermented or aged in, or because nothing is known about how it is packaged). |


---

# Component Types

## HopAbsorptionRate

Typical net retention of wort or beer by hops, for each of the two common forms of hops.  See `hop_absorption_rate` on [Equipment](#equipment) for how other forms map on to these.

<strong>HopAbsorptionRate</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| pellet |  | [Measurement::VolumePerMass](./Measurement.md#volumepermass) | Typical net retention for pellet (and powder) hops. |
| leaf |  | [Measurement::VolumePerMass](./Measurement.md#volumepermass) | Typical net retention for leaf (whole cone) and plug hops. |

## Vessel

An individual vessel (eg mash tun, boil kettle) that forms part of brewing equipment.

<strong>Vessel</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| max_volume | ✅ | [Measurement::Volume](./Measurement.md#volume) | Maximum usable capacity of the vessel.<br /><br />NB: This is the capacity of the vessel, not the volume that is normally used in it (eg it is not a pre-boil or batch volume).  See also `default_batch_size` on [Equipment](#equipment). |
| loss | ✅ | [Measurement::Volume](./Measurement.md#volume) | Volume that does not make it out of this vessel to the next stage -- eg dead space below the outlet, trub, or what is left in a chiller or in pipework.  Where this vessel plays more than one role (eg the kettle in an all-in-one system, which is also where the mash happens), this is the loss when the contents finally leave it.  (For an all-in-one system, anything that does not drain from the malt pipe, other than what the grain absorbs, should be treated as grain absorption.) |
| vessel_type |  | string | Free text type of the vessel, such as its material or model. |
| notes |  | string |  |

## HotSideVessel

A vessel used for the hot-side of brewing.

<strong>HotSideVessel</strong> is a JSON object with all properties from [Vessel](#vessel) as well as these additional ones:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| weight |  | [Measurement::Mass](./Measurement.md#mass) | The weight of the piece of equipment, especially important for when the mash tun is not preheated. |
| specific_heat_capacity |  | [Measurement::SpecificHeatCapacity](./Measurement.md#specificheatcapacity) | The specific heat capacity of the piece of equipment, especially important for when the mash tun is not preheated. |

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

Documentation generated from the [dotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) (v1.2.0) on 2026-11-25 at 14:46:14+0100.
