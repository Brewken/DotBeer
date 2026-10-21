# StockPurchase

Each type of ingredient (Culture, Fermentable, Hop, Misc) has a corresponding stock purchase


---

# Component Types

## StockPurchaseCommon



<strong>StockPurchaseCommon</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| name |  | string | This is typically a short label for the purchase, eg "April visit to LHBS". |
| date_ordered |  | [Measurement::Date](./Measurement.md#date) |  |
| date_received |  | [Measurement::Date](./Measurement.md#date) |  |
| date_best_before |  | [Measurement::Date](./Measurement.md#date) |  |
| supplier |  | string |  |
| note |  | string | This is intended to be a brief note (hence singular *note* rather than *notes* that we use elsewhere for more extensive text). |
| purchase_price |  | [Measurement::CurrencyAmount](./Measurement.md#currencyamount) |  |
| purchase_tax |  | [Measurement::CurrencyAmount](./Measurement.md#currencyamount) |  |
| shipping_cost |  | [Measurement::CurrencyAmount](./Measurement.md#currencyamount) |  |

## StockUseCommon



<strong>StockUseCommon</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| date | ✅ | [Measurement::Date](./Measurement.md#date) |  |
| reason | ✅ | Enum:<br>&nbsp;∙ `used`<br>&nbsp;∙ `lost`<br>&nbsp;∙ `disposed` | `used` is typically use in a recipe<br>`lost` is spillage and spoilage<br>`disposed` means deliberately disposed of (eg given to someone else or thrown away because past sell-by date). |
| name |  | string | This is typically auto-generated, eg "Stock Use #1". |
| brew_log_id |  | [DotBeer::LocalId](./DotBeer.md#localid) | The Local ID of the brew log corresponding to this use.  (Obviously the brew log in question must be in the "brew_logs" section of a recipe the same dotBeer file.) |
| note |  | string |  |

## StockUseCulture



| Property | Required? | Type |
| -------- | --------- | ---- |
| amount_used | ✅ | [Culture::CultureAmount](./Culture.md#cultureamount) |

## StockPurchaseCulture

Note that both `amount_ordered` and `amount_received` need to be the same type of measure.  Eg, it's not supported for one to be mass and the other to be volume.

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| Culture_id | ✅ | [DotBeer::LocalId](./DotBeer.md#localid) | The Local ID of the Culture purchased.  (Obviously the culture in question must be in the "cultures" section of the same dotBeer file.) |
| amount_ordered |  | [Culture::CultureAmount](./Culture.md#cultureamount) |  |
| amount_received |  | [Culture::CultureAmount](./Culture.md#cultureamount) |  |
| stock_uses |  | array of [StockUseCulture](#stockuseculture) |  |

## StockUseFermentable



| Property | Required? | Type |
| -------- | --------- | ---- |
| amount_used | ✅ | [Fermentable::FermentableAmount](./Fermentable.md#fermentableamount) |

## StockPurchaseFermentable

Note that both `amount_ordered` and `amount_received` need to be the same type of measure.  Eg, it's not supported for one to be mass and the other to be volume.

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| fermentable_id | ✅ | [DotBeer::LocalId](./DotBeer.md#localid) | The Local ID of the fermentable purchased.  (Obviously the fermentable in question must be in the "fermentables" section of the same dotBeer file.) |
| amount_ordered |  | [Fermentable::FermentableAmount](./Fermentable.md#fermentableamount) |  |
| amount_received |  | [Fermentable::FermentableAmount](./Fermentable.md#fermentableamount) |  |
| stock_uses |  | array of [StockUseFermentable](#stockusefermentable) |  |

## StockUseHop



| Property | Required? | Type |
| -------- | --------- | ---- |
| amount_used | ✅ | [Hop::HopAmount](./Hop.md#hopamount) |

## StockPurchaseHop

Note that both `amount_ordered` and `amount_received` need to be the same type of measure.  Eg, it's not supported for one to be mass and the other to be volume.

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| hop_id | ✅ | [DotBeer::LocalId](./DotBeer.md#localid) | The Local ID of the hop purchased.  (Obviously the hop in question must be in the "hops" section of the same dotBeer file.) |
| amount_ordered |  | [Hop::HopAmount](./Hop.md#hopamount) |  |
| amount_received |  | [Hop::HopAmount](./Hop.md#hopamount) |  |
| stock_uses |  | array of [StockUseHop](#stockusehop) |  |

## StockUseMisc



| Property | Required? | Type |
| -------- | --------- | ---- |
| amount_used | ✅ | [Misc::MiscAmount](./Misc.md#miscamount) |

## StockPurchaseMisc

Note that both `amount_ordered` and `amount_received` need to be the same type of measure.  Eg, it's not supported for one to be mass and the other to be volume.

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| misc_id | ✅ | [DotBeer::LocalId](./DotBeer.md#localid) | The Local ID of the misc purchased.  (Obviously the misc in question must be in the "miscs" section of the same dotBeer file.) |
| amount_ordered |  | [Misc::MiscAmount](./Misc.md#miscamount) |  |
| amount_received |  | [Misc::MiscAmount](./Misc.md#miscamount) |  |
| stock_uses |  | array of [StockUseMisc](#stockusemisc) |  |



---

Documentation generated from the [dotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) (v0.10.0) on 2026-10-21 at 19:47:37+0200.
