## Description

**Python script checking for duplicate data in a MongoDB database collection. Outputs a list of all duplicates within the collection searching for unique id's with a different modifyDate**

*Task: Look at the ID field in each collection ('data.id' within the json), and determine if there are duplicates.*

*Last Check: Feb 27 2023*

* Initial Findings
	* Duplicates exist in all collections: Dockets, Documents, and Comments
	* The ammount of times each docket/document/comment is duplicated varies. as low as 2 times to 960 (highest I've seen)

* Deeper Exploration
	* Duplicate id's appear because of the data.attributes.modifyDate being different across some entries
		* example: 'data.id': 'VA-2021-VACO-0001'
		* Docket id appears multiple times but the modifyDate is sometimes different
	* However, this is not always the case as there exist duplicates in the data where the modifyDate is the same across entries. Using the same docket as the example prior: 
		* example 1: {'data.id': 'VA-2021-VACO-0001','data.attributes.modifyDate': '2021-12-16T16:57:32Z'} 
		* example 2: {'data.id': 'VA-2021-VACO-0001','data.attributes.modifyDate': '2021-12-17T16:52:03Z'}
		* These Examples use the same docket but instead of modifyDate being unique, is the same across the entries. 
		* Each of these examples is duplicated twice and there seems to be no differentiation amongst them
* Example CLI command to query elements by id and modifyDate

`mongo mirrulations --eval 'db.dockets_2023_02_03.find({"data.id": "VA-2021-VACO-0001", "data.attributes.modifyDate": "2021-12-17T16:52:03Z"}).pretty()'
`

`dockets_2023_02_03`: the collection to query 
add or remove attributes within find({}) to edit query
