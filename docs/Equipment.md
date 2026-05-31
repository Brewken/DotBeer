# Equipment

Groups together all the vessels in a set of brewing equipment.  Note that, in some set-ups, one vessel serves multiple purposes -- eg mash tun and kettle may be the same physical vessel -- but there are nonetheless individual entries here for each "purpose".

<strong>Equipment</strong> is a JSON object with the following properties:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th><th style="border: 1px solid black; padding: 6px;">Description</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
name
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
string
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
kettle
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
[BoilKettle](#boilkettle)
</td><td style="border: 1px solid black; padding: 6px;">
Boil Kettle
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
hlt
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[HotSideVessel](#hotsidevessel)
</td><td style="border: 1px solid black; padding: 6px;">
Hot Liquor Tank
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
mash_tun
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[MashTun](#mashtun)
</td><td style="border: 1px solid black; padding: 6px;">
Mash Tun
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
lauter_tun
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[HotSideVessel](#hotsidevessel)
</td><td style="border: 1px solid black; padding: 6px;">
Lauter Tun
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
fermenter
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Vessel](#vessel)
</td><td style="border: 1px solid black; padding: 6px;">
Fermentation Vessel
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
aging_vessel
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Vessel](#vessel)
</td><td style="border: 1px solid black; padding: 6px;">
Aging Vessel
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
packaging_vessel
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Vessel](#vessel)
</td><td style="border: 1px solid black; padding: 6px;">
Packaging Vessel
</td></tr>


---

# Definitions

## Vessel

An individual vessel (eg mash tun, boil kettle) that forms part of brewing equipment.

<strong>Vessel</strong> is a JSON object with the following properties:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th><th style="border: 1px solid black; padding: 6px;">Description</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
loss
</td><td style="border: 1px solid black; padding: 6px;">
✅
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::Volume](./Measurement.md#volume)
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
vessel_type
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
string
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
max_volume
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::Volume](./Measurement.md#volume)
</td><td style="border: 1px solid black; padding: 6px;">
Maximum usable capacity of the vessel.
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
notes
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
string
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td></tr>

## HotSideVessel

A vessel used for the hot-side of brewing.

<strong>HotSideVessel</strong> is a JSON object with all properties from [Vessel](#vessel) as well as these additional ones:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th><th style="border: 1px solid black; padding: 6px;">Description</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
weight
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::Mass](./Measurement.md#mass)
</td><td style="border: 1px solid black; padding: 6px;">
The weight of the piece of equipment, especially important for when the mash tun is not preheated.
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
specific_heat_capacity
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::SpecificHeatCapacity](./Measurement.md#specificheatcapacity)
</td><td style="border: 1px solid black; padding: 6px;">
The specific heat capacity of the piece of equipment, especially important for when the mash tun is not preheated.
</td></tr>

## MashTun

A hot-side vessel used for the mash.

<strong>MashTun</strong> is a JSON object with all properties from [HotSideVessel](#hotsidevessel) as well as these additional ones:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th><th style="border: 1px solid black; padding: 6px;">Description</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
grain_absorption_rate
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::SpecificVolume](./Measurement.md#specificvolume)
</td><td style="border: 1px solid black; padding: 6px;">
The apparent volume absorbed by grain, typical values are 0.125 qt/lb (1.04 L/kg) for a mash tun, 0.08 gal/lb (0.66 L/kg) for BIAB.
</td></tr>

## BoilKettle

A hot-side vessel used for the boil.

<strong>BoilKettle</strong> is a JSON object with all properties from [HotSideVessel](#hotsidevessel) as well as these additional ones:

<table style="border-collapse: collapse;">
<tr>
<th style="border: 1px solid black; padding: 6px;">Property</th><th style="border: 1px solid black; padding: 6px;">Required?</th><th style="border: 1px solid black; padding: 6px;">Type</th><th style="border: 1px solid black; padding: 6px;">Description</th>
</tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
boil_rate_per_hour
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::Volume](./Measurement.md#volume)
</td><td style="border: 1px solid black; padding: 6px;">
The volume boiled off during 1 hour, measured before and after at room temperature.
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
drain_rate_per_minute
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::Volume](./Measurement.md#volume)
</td><td style="border: 1px solid black; padding: 6px;">
The volume that leaves the kettle, especially important for non-immersion chillers that cool the wort as it leaves the kettle.
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
internalDiameter
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::Length](./Measurement.md#length)
</td><td style="border: 1px solid black; padding: 6px;">
With openingDiameter, allows calculation of IBU by Paul-John Hosom's mIBU formula
</td></tr>
<tr>
<td style="border: 1px solid black; padding: 6px;">
openingDiameter
</td><td style="border: 1px solid black; padding: 6px;">
&nbsp;
</td><td style="border: 1px solid black; padding: 6px;">
[Measurement::Length](./Measurement.md#length)
</td><td style="border: 1px solid black; padding: 6px;">
With internalDiameter, allows calculation of IBU by Paul-John Hosom's mIBU formula
</td></tr>



---

Documentation generated from the [DotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) on 2026-05-31.
