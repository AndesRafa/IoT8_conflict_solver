/**
*   ApiElement
*/
DROP TABLE IF EXISTS ApiElement;
CREATE TABLE ApiElement (
    ApiElementID INTEGER PRIMARY KEY,
    ApiElementName VARCHAR(500),
    ApiElementDescription VARCHAR(500)
);


/**
*   Differential
*/
DROP TABLE IF EXISTS Differential;
CREATE TABLE Differential (
    DifferentialID INTEGER PRIMARY KEY,
    ApiName VARCHAR(500),
    ApiServer VARCHAR(500),
    ApiOldVersion VARCHAR(50),
    ApiNewVersion VARCHAR(50),
    DifferentialTypeID INTEGER,
    ElementPath VARCHAR(500),
    OldElement VARCHAR(500),
    NewElement VARCHAR(500), 

    FOREIGN KEY (DifferentialTypeID) REFERENCES DifferentialType(DifferentialTypeID)
);


/**
*   DifferentialType
*/
DROP TABLE IF EXISTS DifferentialType;
CREATE TABLE DifferentialType (
    DifferentialTypeID INTEGER PRIMARY KEY,
    DifferentialTypeDescription VARCHAR(500)
);


/**
*   Taxonomy
*/
DROP TABLE IF EXISTS Taxonomy;
CREATE TABLE Taxonomy (
    TaxonomyID INTEGER PRIMARY KEY,
    Description VARCHAR(500),
    DifferentialTypeID INTEGER,
    ApiElementID INTEGER,
    AdaptationNodeID INTEGER,

    FOREIGN KEY (DifferentialTypeID)
         REFERENCES DifferentialType(DifferentialTypeID)/*,
    FOREIGN KEY (ApiElementID)
         REFERENCES ApiElement(ApiElementID),
    FOREIGN KEY (AdaptationNodeID)
         REFERENCES Adaptation(AdaptationNodeID)*/
);


/**
*   AdaptationNode
*/
DROP TABLE IF EXISTS AdaptationNode;
CREATE TABLE AdaptationNode (
    AdaptationNodeID INTEGER PRIMARY KEY,
    TaxonomyID INTEGER,
    AdaptationNodeName VARCHAR(100),
    AdaptationNodeDescription VARCHAR(500),
    AdaptationNodeVerb VARCHAR(10),
    AdaptationNodePath VARCHAR(500),
    AdaptationNodeRequest VARCHAR(500),
    AdaptationNodeResponse VARCHAR(500),

    FOREIGN KEY (TaxonomyID) REFERENCES Taxonomy(TaxonomyID)
);


/**
*   DifferentialAdaptation
*/
DROP TABLE IF EXISTS DifferentialAdaptation;
CREATE TABLE DifferentialAdaptation (
    DifferentialAdaptationID INTEGER PRIMARY KEY,
    DifferentialID INTEGER,
    AdaptationNodeID INTEGER,

    FOREIGN KEY (DifferentialID) REFERENCES Differential(DifferentialID),
    FOREIGN KEY (AdaptationNodeID)
        REFERENCES AdaptationNode(AdaptationNodeID)
);
