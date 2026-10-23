# StockPurchase

Each type of ingredient (Culture, Fermentable, Hop, Misc) has a corresponding stock purchase.  A "stock purchase" can actually be any sort of stock acquisition, including by gift or self-production.


---

# Component Types

## StockPurchaseCommon



<strong>StockPurchaseCommon</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| name |  | string | This is typically a short label for the purchase, eg "April visit to LHBS". |
| date_ordered |  | [Measurement::Date](./Measurement.md#date) | The date the stock was ordered. |
| date_received |  | [Measurement::Date](./Measurement.md#date) | The date the stock was received. |
| date_best_before |  | [Measurement::Date](./Measurement.md#date) | The best-before (or use-by) date of the stock. |
| supplier |  | string | The shop or company the stock was acquired from (which need not be the ingredient's producer). |
| note |  | string | This is intended to be a brief note (hence singular *note* rather than *notes* that we use elsewhere for more extensive text). |
| purchase_price |  | [Measurement::CurrencyAmount](./Measurement.md#currencyamount) | Excludes any amount specified in `purchase_tax`.  This field is optional as a "stock purchase" could potentially be a stock acquisition in which no money changed hands. |
| purchase_tax |  | [Measurement::CurrencyAmount](./Measurement.md#currencyamount) | If this is present, then it represents a tax amount (eg sales tax, VAT, import duty) not included in `purchase_price` (and in particular, a `purchase_tax` of zero means no tax was paid on the purchase).  If `purchase_tax` is not present, it means `purchase_price` is inclusive of (an unspecified amount of) tax. |
| shipping_cost |  | [Measurement::CurrencyAmount](./Measurement.md#currencyamount) | This is whatever part of the shipping cost of an order that the brewer (or her brewing software) chooses to allocate to this ingredient purchase. |

## StockUseCommon



<strong>StockUseCommon</strong> is a JSON object with the following properties:

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| date | ✅ | [Measurement::Date](./Measurement.md#date) | The date the stock was used, lost or disposed of. |
| reason | ✅ | Enum:<br>&nbsp;∙ `used`<br>&nbsp;∙ `lost`<br>&nbsp;∙ `disposed` | `used` typically means "used in a recipe"<br>`lost` is spillage and spoilage<br>`disposed` means deliberately disposed of (eg given to someone else or thrown away because past sell-by date). |
| name |  | string | This is typically auto-generated, eg "Stock Use #1". |
| brew_log_id |  | [DotBeer::LocalId](./DotBeer.md#localid) | The Local ID of the brew log corresponding to this use.  (Obviously the brew log in question must be in the "brew_logs" section of a recipe in the same dotBeer file.) |
| note |  | string | A brief note about this use of the stock. |

## StockUseCulture



| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| amount_used | ✅ | [Culture::CultureAmount](./Culture.md#cultureamount) | The amount used, lost or disposed of. |

## StockPurchaseCulture

Note that both `amount_ordered` and `amount_received` need to be the same type of measure.  Eg, it's not supported for one to be mass and the other to be volume.

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| culture_id | ✅ | [DotBeer::LocalId](./DotBeer.md#localid) | The Local ID of the Culture purchased.  (Obviously the culture in question must be in the "cultures" section of the same dotBeer file.) |
| amount_ordered |  | [Culture::CultureAmount](./Culture.md#cultureamount) | The amount ordered. |
| amount_received |  | [Culture::CultureAmount](./Culture.md#cultureamount) | The amount actually received (which may differ from the amount ordered). |
| stock_uses |  | array of [StockUseCulture](#stockuseculture) | What was subsequently done with this stock (eg used in a brew, lost or disposed of). |

## StockUseFermentable



| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| amount_used | ✅ | [Fermentable::FermentableAmount](./Fermentable.md#fermentableamount) | The amount used, lost or disposed of. |

## StockPurchaseFermentable

Note that both `amount_ordered` and `amount_received` need to be the same type of measure.  Eg, it's not supported for one to be mass and the other to be volume.

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| fermentable_id | ✅ | [DotBeer::LocalId](./DotBeer.md#localid) | The Local ID of the fermentable purchased.  (Obviously the fermentable in question must be in the "fermentables" section of the same dotBeer file.) |
| amount_ordered |  | [Fermentable::FermentableAmount](./Fermentable.md#fermentableamount) | The amount ordered. |
| amount_received |  | [Fermentable::FermentableAmount](./Fermentable.md#fermentableamount) | The amount actually received (which may differ from the amount ordered). |
| stock_uses |  | array of [StockUseFermentable](#stockusefermentable) | What was subsequently done with this stock (eg used in a brew, lost or disposed of). |

## StockUseHop



| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| amount_used | ✅ | [Hop::HopAmount](./Hop.md#hopamount) | The amount used, lost or disposed of. |

## StockPurchaseHop

Note that both `amount_ordered` and `amount_received` need to be the same type of measure.  Eg, it's not supported for one to be mass and the other to be volume.

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| hop_id | ✅ | [DotBeer::LocalId](./DotBeer.md#localid) | The Local ID of the hop purchased.  (Obviously the hop in question must be in the "hops" section of the same dotBeer file.) |
| amount_ordered |  | [Hop::HopAmount](./Hop.md#hopamount) | The amount ordered. |
| amount_received |  | [Hop::HopAmount](./Hop.md#hopamount) | The amount actually received (which may differ from the amount ordered). |
| stock_uses |  | array of [StockUseHop](#stockusehop) | What was subsequently done with this stock (eg used in a brew, lost or disposed of). |

## StockUseMisc



| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| amount_used | ✅ | [Misc::MiscAmount](./Misc.md#miscamount) | The amount used, lost or disposed of. |

## StockPurchaseMisc

Note that both `amount_ordered` and `amount_received` need to be the same type of measure.  Eg, it's not supported for one to be mass and the other to be volume.

| Property | Required? | Type | Description |
| -------- | --------- | ---- | ----------- |
| misc_id | ✅ | [DotBeer::LocalId](./DotBeer.md#localid) | The Local ID of the misc purchased.  (Obviously the misc in question must be in the "miscs" section of the same dotBeer file.) |
| amount_ordered |  | [Misc::MiscAmount](./Misc.md#miscamount) | The amount ordered. |
| amount_received |  | [Misc::MiscAmount](./Misc.md#miscamount) | The amount actually received (which may differ from the amount ordered). |
| stock_uses |  | array of [StockUseMisc](#stockusemisc) | What was subsequently done with this stock (eg used in a brew, lost or disposed of). |



---

Documentation generated from the [dotBeer schema](https://github.com/Brewken/DotBeer/tree/main/schema) (v1.0.0) on 2026-10-23 at 21:45:26+0200.
