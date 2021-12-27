# Acme Widget Co. Sales System POC

**Table of contents**
- [Requirements](#requirements)
- [Getting Started](#getting-started)
- [Assumptions Made](#assumptions-made)
- [Scope of Improvements](#scope-of-improvements)

## Requirements
This POC is tested with:

|         | Version |
| ------- | ------- |
| Python  | 3.9.7   |

## Getting Started

1. Clone this repository.
2. Create multiple products using Product class.
3. Add these above created products into product catalogue using ProductService class methods.
4. Inside ProductService delivery charges and offers rules are defined.
5. Once the Product Catalogue is ready, we can create multiple basket with 
    different set of products to it and get total amount.
6. Total amount is calculated after applying offers first and then delivery charges.
> Note: Examples are shown in run.py file on how to use it.

## Assumptions Made
1. Only one store is available for the client.
2. Multiple offers can be applied at the same time.
3. Apply all the offers in the basket first, before calculating the delivery charges.
4. After applying all the offers, delivery charges should be calculated.
5. We can add multiple offers.

## Scope of Improvements
1. Only one offer can be applied.
2. Offers should have separate service.
3. In case of multiple stores, we can have a store model and service where we can add
    different product catalogue and different offers for different stores.
