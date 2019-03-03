---
layout: post
categories:
  - thesis
---

To store the collected data without hickups, a small systems needs to be designed.

Both the Structure Core and Intel RealSense D435i will be attached to a robotic arm, the Hogeschool van Amsterdam's ABB IRB 4600-60/2.05.  Using my own laptop to stay within cable range of the sensors will not be sufficient, as the sensors will move fast (to see the influence of inertia), and over a rather long distance (the arm is 2.05 m long from the base to its end effector).  The sensors do not support a bus type that is wired through the arm itself.  That means that a system for data collection needs to be attached to the arm itself.

First I will make a rough estimate of the data collected per time unit from the sensors.  Then I will list the technical requirements of a data collection system.

## Raw data per second

Structure is more transparant on their website about the generated data per second than Intel.  The Core caputes depth images with a resolution of 1280×800 px @ 60 Hz.  Assuming each pixel is stored as a single byte, that means $$1280 \cdot 800 \cdot 60 = 61 440~kB/s$$.  The RGB camera captures images with a resolution 640×480 px at a maximum of 100 Hz.  However, RGB and D cameras will be synchronized, so it sill be $$640 \cdot 480 \cdot 60 = 55 296~kB/s$$.  The IMU generates 6 `double`s (`sizeof(double) == 8`) with max. 1000 Hz, so that is $$6 \cdot 8 \cdot 1000 = 48~kB/s$$.  Summed, the data collector would need to be able to record $$116.784~MB/s$$, not accounting for any metadata such as timestamps.

The RealSense D435i could generate depth images of 1280×720 px @ 90 Hz ( $$82 944~kB/s$$ ) and color images of 1920×1080 @ 30 Hz ( $$186 624~kB/s$$ ).  They give no indication on the IMU used, so I will, for this handwavy guesstimate of needed bandwith, the same value as for the Core ( $$48~kB/s$$ ).  That is a significant $$269.616~MB/s$$ at most.

### Metadata per frame

Metadata I am interested in, consists of the (`double`) timestamp ( $$8~B/frame$$ ) and the type of the frame (one of four options).  The frame type will most easily be stored as a `char` of 1 byte.  That leaves us with $$9~B/frame$$.  In above examples, this would be $$9 \cdot (60 + 60 + 1000 + 1000) = 19.08~kB/s$$ for the Core and $$9 \cdot (90 + 30 + 1000 + 1000) = 19.08~kB/s$$ for the D435i.  This increases their total data writing requirements to $$116.803~MB/s$$ and $$269.635~MB/s$$, respectively.


## Technical specifications

Requirements for the data collector are as follows:

1. **The system must be small and light.**  The system needs to be mounted on the arm, near the end effector.  In that region is not much space to securely mount a larger, heavier system.  Most probably this would mean a singl-board computer (SBC).
2. **The system must have GPIO pins.** This is to make sure it can have any external synchronization triggers that I might want to add later.
3. **The system must have at least 1, and desirably 2 USB 3.0 or higher connectors.  Each connector must be on a separate bus.**  The two buses is to exclude any possible bus overload because of the amount of data sent by both sensors.
4. **The system must have a separate storage medium from its boot medium.**  This will ensure that the required data write speeds will be attained, and independently read or write to the storage medium.
5. **The storage medium must be an SSD.**  Most SBCs only have connectors for SD or eMMC media.  When SD is supported, it is often unclear if UHS-II (≤ 312 MB/s) or higher is supported.  UHS-I (≤ 104 MB/s) is too slow.  In ODROID's speed comparison for the ODROID-XU4 [of SD vs. eMMC writing and reading speeds](https://www.hardkernel.com/shop/128gb-emmc-module-xu4-linux/), their eMMC v5.0 memory's $$39.3~MB/s$$ write speed is still much too slow.  On the other hand, Samsung's 970 EVO and 970 EVO Plus line SSDs seem fast enough in [a speed test by Tweakers.net](https://tweakers.net/reviews/6824/3/samsung-970-evo-plus-populaire-serie-op-herhaling-resultaten.html), even for 2 sensor data streams.

I have looked at several systems:

| System name | Satisfied requirement # |
|:------------|:------------------------|
| [Raspberry Pi 3 Model B+](https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/) | 1, 2, 4 |
| [ODROID-XU4](https://www.hardkernel.com/shop/odroid-xu4/) | 1, 2, 3, 4 |
| [LattePanda 4G/64G](https://www.lattepanda.com/products/3.html) | 1, 2, 3, 4 |
| [Pine64 RockPro64](https://www.pine64.org/?page_id=61454) | 1, 2, 3, 4, 5 |
| [UDOO X86](https://www.udoo.org/udoo-x86/) Ultra and Advanced Plus | 1, 2, 3, 4, 5 | 
| [Vamrs Rock960](https://www.96boards.org/product/rock960/) | 1, 2, 3, 4, 5 |

Only 3 considered systems fulfill all requirements.  To make a further decision, I will make a parts list for the Pine64 RockPro64, UDOO X86 Ultra, UDOO X86 Advanced Plus, and Vamrs Rock960.

All these prices exclude an SSD, such as the [Samsung 970 Evo Plus 250GB](https://tweakers.net/pricewatch/1303742/samsung-970-evo-plus-250gb.html) for €84.95 including shipping.

### Pine RockPro64

| Part name | Piece price | Pieces | Total |
|:----------|------------:|:------:|------:|
| [ROCKPro64 4GB Single Board Computer](https://www.pine64.org/?product=rockpro64-4gb-single-board-computer) | $79.99 | 1 | $79.99 |
| [ROCKPro64 12V 5A EU POWER SUPPLY](https://www.pine64.org/?product=rockpro64-12v-5a-eu-power-supply) | $12.99 | 1 | $12.99 | 
| [USB Adapter for eMMC Module](https://www.pine64.org/?product=usb-adapter-for-emmc-module) | $4.99 | 1 | $4.99 |
| [32GB eMMC Module](https://www.pine64.org/?product=32gb-emmc) | $24.95 | 1 | $24.95 |
| [ROCKPro64 PCI-e X4 to M.2/NGFF NVMe SSD Interface Card](https://www.pine64.org/?product=rockpro64-pci-e-x4-to-m-2ngff-nvme-ssd-interface-card) | $5.99 | 1 | $5.99 |
| [Fan for ROCKPro64 20mm Mid Profile Heatsink](https://www.pine64.org/?product=fan-for-rockpro64-20mm-mid-profile-heatsink) | $2.99 | 1 | $2.99 |
| [RP64-AI-Case1 	ROCKPro64 PREMIUM ALUMINUM CASING](https://www.pine64.org/?product=rockpro64-premium-aluminum-casing) | $14.99 | 1 | $14.99
| Express shipping | $30.00 | 1 | $30.00 |

Total: $176.89

### UDOO X86
At the time, only the Advanced Plus is in stock.  It is not indicated when the Ultra will be back in stock.

| Part name | Piece price | Pieces | Total |
|:----------|------------:|:------:|------:|
| [UDOO X86 ADVANCED PLUS](https://shop.udoo.org/eu/x86/udoo-x86-advanced-plus.html) | $174.00 | 1 | $174.00 |
| [UDOO X86 METAL CASE](https://shop.udoo.org/eu/catalog/product/view/id/99/s/udoo-x86-metal-case/category/3/) | $23.80 | 1 | $23.80 |
| [Power Supply EU](https://shop.udoo.org/eu/catalog/product/view/id/11/s/power-adapter-eu/category/3/) | $8.90 | 1 | $8.90 |
| Shipping & Handling | $8.00 | 1 | $8.00 |
| Tax | $47.23 | 1 | $47.23 |

Total: $261.93

### Vamrs Rock960

| Part name | Piece price | Pieces | Total |
|:----------|------------:|:------:|------:|
| [ROCK960 - 4GB/32GB / Acrylic](https://store.vamrs.com/products/rock960?variant=1349858164755) | $139.00 | 1 | $139.00 |
| [eMMC Module - 32GB](https://store.vamrs.com/products/emmc-module?variant=12483308748885) | $23.99 | 1 | $23.99 |
| [Metal case for ROCK960 modelA/B](https://store.vamrs.com/products/metal-case-for-rock960?variant=12607133843541) | 29.90 | 1 | $29.90 |
| DHL (express?) shipping | $30.00 | 1 | $30.00 |

Total: $222.89, excluding power supply (12V @ 2A, approx. €15 to [€30](https://nl.farnell.com/ideal-power/25hk-ay-120a200-cp/adaptor-ac-dc-12v-2a/dp/2725680?pf=111782139%2C111782197%2C110166990&krypto=lKvUMUtZEg3Jx6KCx7Us1GqnQctes7NTvBSotizQlnMW3LWilFINzdbDAtZjAh7uWLYweJ8jROwdIIwieIrVqebnhq4soCY3UfLHbuvtRbHtDbJ1%2FDdarVyzGNepnzsZjZSAKu%2BMspDbu11xxAZYZg%2BTKICIdJmGO1J8i%2Fu0xuJA1t0GIF0MDqrhvOfhyMfds8C%2B9oFN0xTqus8iblEjEVsNgTdUsgtI6Bxz76O7mj6uQ56BccsKkU8zp2RtxNYGeFzg%2FbrUXS%2FmIkdbdPc3xVpO7V7GjEtlE3NSxaXcUTcHQvpaOpyg5gvW%2FbBIDkc97RHaPeUj7eSOP5uojmJWVE1KnLgdNcEWOwCzciatB%2BdyRZYxtrFQ3xY0kwrYEtU63MAFaAUKIYrpyk%2F3LzmSknNRHH75piAD9hCoE7sK0uWGhbOlWbkYtiUwCYCCF4UFUpA%2F3DjLZcy0IGDNkQJLxl8haJdH%2BgUrCIVuS7iipj68eaT3vp%2Fyzvt%2BY9M89xBEPFqFpGdQZa9gOOXcpB7Diq%2BafzzHmF%2B%2BnjnfxgaBNeFwNqAkr%2BwN8LOCVZaf0LJsxt9e1f61doWDKJbREw4penp6tE1%2BoJkG5VOcz8C1fBNz%2BXHQjH5fiq%2BKfazeuBjIbuAAlDq056HUwRlvto%2Ba9B7ykLZFk2D4sN2UTTbrMUPaIjr%2FqEqSKjHE5f%2FlD%2BDy5vjugU2rw5xrJhmBT8inCMsL7NGCALkTWAK%2BagqF2Y06ERzGrCRU6t6tTkJefH8n8v7q1n%2Fkx1OrdESOD9YuWa%2BHKv6yJd9xwjNBN0XvLHHsFNvrMCNpnFqEkk2l3rJlp1Nh4VX7qHIGH9wmG1Uac55dAETx7B0%2FT7NMXk6Wfy3JpSxDcYvpfo1XcxNqvMXNMrZ7g5ngffJkSxSluhSHQUSxi1ktDaTADhu%2FLu6fBEUhcYpRMrMWcOic49g2%2FpxqXS%2FIjzu9f9fJCdHylPMnKyqifi3RVe0zmVdM4RwSsm%2BqC1FgNvRXQuZhTwP1j8rJsUnOyWdt93YwGkmJ2YyzfAtDzCGJWefyrgLuSWbCWS4RPApbYDzxLPG26W4exaCvVEeEKca6aaRux3P4IKgubvLwNR4du7yryK51MaqQEUEqAbNO%2FNFV%2Fw8%2FMxqqsFYawfl7qhdn5ZzS9lVY8TPLpvnrnQkocYuxeif8h2misifhq6p42IqWUeBi1i8iljTEIqokfG0pr9fvGnbAhRi3wHSq2DLFNFLxnImGEPUeViXaGHvyLMxuQS5Nci5PhDw4UBEc2dR53NPoU5s%2F6XOWM9Mp%2Fv2Mhf%2F3HTg9ppj2awWzB1dEMYlm1V17yTLP3u0bkpy5Xz1j781zDSaC3CnlzZDdIUCl%2FQxCS52VozW8o1t40ENsI9VTDPEM2IJ7hy8bZam%2FZQSVcL7nCmPFVVvgSsuGNOjwDxmca4Ay2VGShJR45FdeLQKy%2B2f%2BzmoS9pNUMBOSqmiRgPT12A3BOhogedWYqVSbEUOqCue7PNu1MwG2ydX98nBh9HJqYoJepSnifzCK3qSNPUQLhIH1tHZdMmZSfwArbNSu4w7BMKkV5VfvEdGqcrJe8EImv7%2FlaFhOJGfsBgkyuy%2FKosyIN7e0QOQZtc5FVXPLnTRbl4CgyUJM9Xl6wnWO1VGvv54lJxV3%2BkJMm%2FchAD%2FphNqn%2BLYZigDCV6M%2BA3u5cjk4mlZc3Q6JLNqh%2Bkt1KhEb0AhlF%2BBgWZG9b8qWiUm7qsMae0Vm%2FffG8hqx3UbdTeEU2hSFMXst%2BZbI%2FViZ9VVUOrF2RHrrTv1oTIwDuZ2T8Ckf73ZL0ljPvhPzxS3K0GI2Sl0%2Fvql0CFwlYbm0yRobrcSelsns&ddkey=https%3Anl-NL%2FElement14_Netherlands%2Fw%2Fc%2Fpower-line-protection%2Fpower-supplies%2Fac-dc-converters%2Fac-dc-external-plug-in-adaptor-power-supplies))

## Preferred solution
My preferences goes out to the UDOO, as that board has an x86 architecture, which makes it easier to find compatible and pre-compiled packages, when compared with the other two ARMs.

The UDOO has 3 USB 3.0 connectors, but it is unclear how the host layout is organized.  If this will be the ordered product, I will contact the developers for this information.

As a second option, I would go for the RockPro64.  The device has some years of LTS to go (2023), and seems better documented than the Rock960.  In this case, I might consider two collector systems, so that the sensors can collect data from the same run.
