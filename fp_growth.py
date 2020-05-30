import preprocess as pp
import fp_tree

class FPGrowth:
    def __init__(self, min_length, min_support):
        self.min_length = min_length
        self.min_support = min_support

    def frequent_itemsets(self, transactions):
        # Preprocess transactions
        # Filter out those items that do not show up at least min_support times
        # Sort items per transaction in order of frequency (highest to lowest)
        filtered_transactions, filtered_counts = pp.preprocess(
            transactions, self.min_support)

        # Construct FPTree
        tree = fp_tree.FPTree()
        for t in filtered_transactions:
            tree.add(t)

        # Generate itemsets 
        for itemset, support in self._itemsets_with_suffix(tree, []):
            yield itemset, support

    def _itemsets_with_suffix(self, tree, suffix):
        for item in tree.items():
            support = sum(n.count for n in tree.nodes(item))
            if support >= self.min_support and item not in suffix:
                temp = [item] + suffix 
                if len(temp) >= self.min_length:
                    yield (temp, support)

                cond_tree = self._conditional_tree(tree.prefix_paths_with_supports(item))
                for result in self._itemsets_with_suffix(cond_tree, temp):
                    yield result

    def _conditional_tree(self, prefix_paths_with_suppports):
        tree = fp_tree.FPTree()
        for path, support in prefix_paths_with_suppports:
            tree.add(path, support)
        return tree
