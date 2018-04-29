class Taxonomy():

    def __init__(self,
                TaxonomyID=0,
                Description='',
                DifferentialTypeID=0,
                ApiElementID=0,
                AdaptationNodeID=0,
            ):

        self.TaxonomyID = TaxonomyID
        self.Description = Description
        self.DifferentialTypeID = DifferentialTypeID
        self.ApiElementID = ApiElementID
        self.AdaptationNodeID = AdaptationNodeID

        if not TaxonomyID > 0:
            delattr(self, 'TaxonomyID')
