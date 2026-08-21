# Equipment

Groups together all the vessels in a set of brewing equipment.  Note that, in some set-ups, one vessel serves multiple purposes -- eg mash tun and kettle may be the same physical vessel -- but there are nonetheless individual entries here for each "purpose".

<strong>Equipment</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| name | ✅ | string |  |
| kettle | ✅ | [BoilKettle](#boilkettle) | Boil Kettle |
| folder_path |  | [DotBeer::FolderPath](./DotBeer.md#folderpath) | The suggested slash-delimited subfolder path in which to store this Equipment object. |
| hlt |  | [HotSideVessel](#hotsidevessel) | Hot Liquor Tank |
| mash_tun |  | [MashTun](#mashtun) | Mash Tun |
| lauter_tun |  | [HotSideVessel](#hotsidevessel) | Lauter Tun |
| fermenter |  | [Vessel](#vessel) | Fermentation Vessel |
| aging_vessel |  | [Vessel](#vessel) | Aging Vessel |
| packaging_vessel |  | [Vessel](#vessel) | Packaging Vessel |


---

# Component Types

## Vessel

An individual vessel (eg mash tun, boil kettle) that forms part of brewing equipment.

<strong>Vessel</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| loss | ✅ | [Measurement::Volume](./Measurement.md#volume) |  |
| vessel_type |  | string |  |
| max_volume |  | [Measurement::Volume](./Measurement.md#volume) | Maximum usable capacity of the vessel. |
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
| grain_absorption_rate |  | [Measurement::SpecificVolume](./Measurement.md#specificvolume) | The apparent volume absorbed by grain, typical values are 0.125 qt/lb (1.04 L/kg) for a mash tun, 0.08 gal/lb (0.66 L/kg) for BIAB. |

## BoilKettle

A hot-side vessel used for the boil.

<strong>BoilKettle</strong> is a JSON object with all properties from [HotSideVessel](#hotsidevessel) as well as these additional ones:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| boil_rate_per_hour |  | [Measurement::Volume](./Measurement.md#volume) | The volume boiled off during 1 hour, measured before and after at room temperature. |
| drain_rate_per_minute |  | [Measurement::Volume](./Measurement.md#volume) | The volume that leaves the kettle, especially important for non-immersion chillers that cool the wort as it leaves the kettle. |
| internalDiameter |  | [Measurement::Length](./Measurement.md#length) | With openingDiameter, allows calculation of IBU by Paul-John Hosom's mIBU formula |
| openingDiameter |  | [Measurement::Length](./Measurement.md#length) | With internalDiameter, allows calculation of IBU by Paul-John Hosom's mIBU formula |



---

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) (v0.5.0) on 2026-08-21 at 09:19:16+0200.
