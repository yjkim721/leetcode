class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candies = [1] * len(ratings)

        sorted_ratings = sorted(ratings)
        ranks = []
        for i, value in enumerate(sorted_ratings):
            r = ratings.index(value)
            ranks.append(r)
            ratings[r] = -1 * ratings[r]
        ratings = [r * -1 for r in ratings]

        for i in ranks:
            if i + 1 < len(ratings):
                if ratings[i] > ratings[i+1]:
                    candies[i] = candies[i+1] + 1
            if i - 1 >= 0:
                if ratings[i-1] < ratings[i]:
                    candies[i] = max(candies[i-1] + 1, candies[i])
        return sum(candies)

