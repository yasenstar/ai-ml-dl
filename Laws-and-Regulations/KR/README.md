# Load KR "Basic Act" into Graph

Use multiple relationships merge to prevent creating duplicated `:HAVE` relation:

```cypher
MATCH (r:Regulations {name: "Basic Act"})
LOAD CSV WITH HEADERS FROM 'file:///D://GitHub//ai-ml-dl//Laws-and-Regulations//KR//SouthKorea_AI_Basic-Act.csv' AS row
MERGE (c:Chapter {chapterId: row.ChapterID})
SET c.chapterContent = row.ChapterContent, c.chapterContentOriginal = row.ChapterContentOriginal
MERGE (a:Article {articleId: row.ArticleID})
SET a.articleContent = row.ArticleContent, a.articleContentOriginal = row.ArticleContentOriginal
MERGE (p:Paragraph {paragraphId: row.ParagraphID})
SET p.paragraphContent = row.ParagraphContent, p.paragraphContentOriginal = row.ParagraphContentOriginal
MERGE (i:Item {itemId: row.ItemID})
SET i.itemContent = row.ItemContent, i.itemContentOriginal = row.ItemContentOriginal
MERGE (r)-[h1:HAVE]->(c)
MERGE (c)-[h2:HAVE]->(a)
MERGE (a)-[h3:HAVE]->(p)
MERGE (p)-[h4:HAVE]->(i)
RETURN r,c,a,p,i,h1,h2,h3,h4
```

