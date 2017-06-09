"""Tiered Lists - a simple way to group items into tiers (at insertion time) while maintaining uniqueness."""

class TieredLists(object):

    def __init__(self, tiers):
        self.tiers = sorted(tiers, reverse=True)
        self.bags = {}
        for t in self.tiers:
            self.bags[t] = set()

    def get_tier(self, key):
        """Determine in which tier a key should be inserted.
        Returns
        -------
        int
            if the value is greater than at least one of the tiers
        None
            if the value is less than the least tier."""
        tier = None
        for t in self.tiers:
            if key >= t:
                tier = t
                break
        return tier


    def add(self, key, value):
        """Adds a value to a tier based upon where key fits in the tiers
        Parameters
        ----------
        key : int
            used to select the tier into which this value will be inserted
        value : basestring
            to be inserted in the set for the tier.

        Returns
        -------
        int
            int identifying into which tier the item was inserted. None if the key was too low for the lowest tier."""
        tier = self.get_tier(key)
        if tier is not None:
            self.bags[tier].add(value)
        return tier

    def bag(self, tier):
        return self.bags[tier]

    def __str__(self):
        msg = "{{ tiers: {}, bags: {{".format(self.tiers)
        for t, vals in sorted(self.bags.items(), reverse=True):
            msg += "\n{}: {}, {}".format(t, len(vals), vals)
        msg += "} }"
        return msg