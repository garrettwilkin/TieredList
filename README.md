# TieredList
A simple data structure for grouping items based on tiered integer ranges.

## Simple example

Set thresholds:

```
import TieredLists

tiers = [2, 4, 8, 16]
tl = TieredLists(tiers)
```

Add items:

```
path_1 = '/a/short/url'
path_2 = '/the/quick/brown/fox/is/dead'
path_3 = '/news/bangor/2017/06/05/reality-winner/'
tl.add(2, path_1)
tl.add(20, path_2)
```


## Practical usage

Here we can determine how many stories are performing at different levels:

  - twice a minute
  - once a minute
  - once every 2 minutes
  - once every 6 minutes
  - once every 15 minutes


```
if __name__ == '__main__':
    # This is a GA360 analytics client. Library not included here.
    analytics = connect()
    
    # Trying out different tiers to see where our stories tended to fall in terms of popularity (page views).
    # 60 pageviews per thirty minutes is a reasonable top tier for our content.
    # There are regularly 500+ paths with one or two pageviews. Filter those out by setting 4 as the lowest tier.
    tiers = [4,8,16,32,64]

    # Check analytics for 60 reptitions of 10 minute intervals
    loops = 60
    duration = 600
    
    run_tiers = []
    for l in range(loops):
        # Show the current time, just to assist review of the logs at a later date.
        print("{}".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        results = get_realtime_posts(analytics)
        if not results:
            raise ValueError("GA360 realtime returned zero results.")
        else:
            tl = TieredLists(tiers)
            for [path, views] in results:
                # The the path to the TieredList, using the pageviews value to determine a tier.
                tl.add(int(views), path)
            run_tiers.append((l, tl))
        print(tl)
        time.sleep(duration)

```
