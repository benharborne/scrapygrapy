## [0.7.0-beta.3](https://github.com/VinciGit00/Scrapegraph-ai/compare/v0.7.0-beta.2...v0.7.0-beta.3) (2024-05-03)


### Features

* add pdf scraper ([10a9453](https://github.com/VinciGit00/Scrapegraph-ai/commit/10a94530e3fd4dfde933ecfa96cb3e21df72e606))

## [0.7.0-beta.2](https://github.com/VinciGit00/Scrapegraph-ai/compare/v0.7.0-beta.1...v0.7.0-beta.2) (2024-05-03)


### Features

* Azure implementation + embeddings refactoring ([aa9271e](https://github.com/VinciGit00/Scrapegraph-ai/commit/aa9271e7bc4daa54860499d0615580b17550ff58))


### Refactor

* Changed the way embedding model is created in AbstractGraph class and removed handling of embedding model creation from RAGNode. Now AbstractGraph will call a dedicated method for embedding models instead of _create_llm. This makes it easy to use any LLM with any supported embedding model. ([819cbcd](https://github.com/VinciGit00/Scrapegraph-ai/commit/819cbcd3be1a8cb195de0b44c6b6d4d824e2a42a))

## [0.7.0-beta.1](https://github.com/VinciGit00/Scrapegraph-ai/compare/v0.6.2...v0.7.0-beta.1) (2024-05-03)


### Features

* add base_node to __init__.py ([cb1cb61](https://github.com/VinciGit00/Scrapegraph-ai/commit/cb1cb616b7998d3624bf57b19b5f1b1945fea4ef))

## [0.6.2](https://github.com/VinciGit00/Scrapegraph-ai/compare/v0.6.1...v0.6.2) (2024-05-02)


### Bug Fixes

* add to requirements.txt langchain-aws = "^0.1.2" ([1afa319](https://github.com/VinciGit00/Scrapegraph-ai/commit/1afa31910d25b2735abe0ad09dad433d6c2159fb))


### Docs

* **tree:** added roadmap ([c8eeff8](https://github.com/VinciGit00/Scrapegraph-ai/commit/c8eeff873db6c8d23c9e4109ddee46edaa68b92b))
* **roadmap:** open contributions ([4441505](https://github.com/VinciGit00/Scrapegraph-ai/commit/4441505b239fa819032469f148115bb3392b15ea))
* typo ([faa3498](https://github.com/VinciGit00/Scrapegraph-ai/commit/faa3498fa7694ee3309eeed479d8f1bc4b1c7b97))


### CI

* **release:** 0.6.1-beta.1 [skip ci] ([75a4042](https://github.com/VinciGit00/Scrapegraph-ai/commit/75a4042a232a5b69fd38d1666fea9633b4fd015e))

## [0.6.1](https://github.com/VinciGit00/Scrapegraph-ai/compare/v0.6.0...v0.6.1) (2024-05-02)



### Bug Fixes

* gemini errror ([2ea54ea](https://github.com/VinciGit00/Scrapegraph-ai/commit/2ea54eab1d070e177c7d5ecfcc032b325fbd7c12))


## [0.6.0](https://github.com/VinciGit00/Scrapegraph-ai/compare/v0.5.2...v0.6.0) (2024-05-02)


### Features

* added node and graph for CSV scraping ([4d542a8](https://github.com/VinciGit00/Scrapegraph-ai/commit/4d542a88f7d949a5ba360dcd880716c8110a5d14))
* Allow end users to pass model instances for llm and embedding model ([b86aac2](https://github.com/VinciGit00/Scrapegraph-ai/commit/b86aac2188887642564a34d13d55d0fcff220ec1))
* modified node name ([02d1af0](https://github.com/VinciGit00/Scrapegraph-ai/commit/02d1af006cb89bf860ee4f1186f582e2049a8e3d))


### CI

* **release:** 0.5.0-beta.7 [skip ci] ([40b2a34](https://github.com/VinciGit00/Scrapegraph-ai/commit/40b2a346d57865ca21915ecaa658096c52a2cc6b))
* **release:** 0.5.0-beta.8 [skip ci] ([c11331a](https://github.com/VinciGit00/Scrapegraph-ai/commit/c11331a26ac325dfcf489272442ceeed13225a39))

## [0.5.2](https://github.com/VinciGit00/Scrapegraph-ai/compare/v0.5.1...v0.5.2) (2024-05-02)


### Bug Fixes

* bug on script_creator_graph.py ([4a3bc37](https://github.com/VinciGit00/Scrapegraph-ai/commit/4a3bc37f2fbb24953edd68f28234ff14302ac120))

## [0.5.1](https://github.com/VinciGit00/Scrapegraph-ai/compare/v0.5.0...v0.5.1) (2024-05-02)


### Bug Fixes

* examples and graphs ([5cf4e4f](https://github.com/VinciGit00/Scrapegraph-ai/commit/5cf4e4f92f024041c44211aebd2e3bdf73351a00))


### Docs

* added venv suggestion ([ba2b24b](https://github.com/VinciGit00/Scrapegraph-ai/commit/ba2b24b4cd82d63f9235051eb0e95519c51fd639))
* base and fetch node ([e981796](https://github.com/VinciGit00/Scrapegraph-ai/commit/e9817963c8e98e35662cc5a140b0348792d25307))
* change contributing.md with new ci/cd workflow ([3e91a46](https://github.com/VinciGit00/Scrapegraph-ai/commit/3e91a46522ab1f6b2f733efd234b06df4687c695))
* fixed basegraph docstring ([29427c2](https://github.com/VinciGit00/Scrapegraph-ai/commit/29427c233485816967c4ecd6c1951351be9b27ce))
* graphs and helpers docstrings ([0631985](https://github.com/VinciGit00/Scrapegraph-ai/commit/0631985e6156bd21ec5317faff9e345c8aa7f88b))
* refactor examples ([c11fc28](https://github.com/VinciGit00/Scrapegraph-ai/commit/c11fc288963e1a2818e451279a3bf53eb33e22be))
* refactor models docstrings ([18c20eb](https://github.com/VinciGit00/Scrapegraph-ai/commit/18c20eb03de183a0311be5ffe21f53ec4edf1b87))
* refactor nodes docstrings ([1409797](https://github.com/VinciGit00/Scrapegraph-ai/commit/140979747598210674131befadd786800c9fb5ec))
* update utils docstrings ([cf038b3](https://github.com/VinciGit00/Scrapegraph-ai/commit/cf038b33eaae42f65d7d9c782b5729092b272dd0))

## [0.5.0](https://github.com/VinciGit00/Scrapegraph-ai/compare/v0.4.1...v0.5.0) (2024-04-30)


### Features

* add cluade integration ([e0ffc83](https://github.com/VinciGit00/Scrapegraph-ai/commit/e0ffc838b06c0f024026a275fc7f7b4243ad5cf9))
* add co-author ([719a353](https://github.com/VinciGit00/Scrapegraph-ai/commit/719a353410992cc96f46ec984a5d3ec372e71ad2))
* **fetch:** added playwright support ([42ab0aa](https://github.com/VinciGit00/Scrapegraph-ai/commit/42ab0aa1d275b5798ab6fc9feea575fe59b6e767))
* added verbose flag to suppress print statements ([2dd7817](https://github.com/VinciGit00/Scrapegraph-ai/commit/2dd7817cfb37cfbeb7e65b3a24655ab238f48026))
* base groq + requirements + toml update with groq ([7dd5b1a](https://github.com/VinciGit00/Scrapegraph-ai/commit/7dd5b1a03327750ffa5b2fb647eda6359edd1fc2))
* **refactor:** changed variable names ([8fba7e5](https://github.com/VinciGit00/Scrapegraph-ai/commit/8fba7e5490f916b325588443bba3fff5c0733c17))
* **llm:** implemented groq model ([dbbf10f](https://github.com/VinciGit00/Scrapegraph-ai/commit/dbbf10fc77b34d99d64c6cd7f74524b6d8e57fa5))
* updated requirements.txt ([d368725](https://github.com/VinciGit00/Scrapegraph-ai/commit/d36872518a6d234eba5f8b7ddca7da93797874b2))


### Bug Fixes

* script generator and add new benchmarks ([e3d0194](https://github.com/VinciGit00/Scrapegraph-ai/commit/e3d0194dc93b20dc254fc48bba11559bf8a3a185))


### CI

* **release:** 0.4.0-beta.3 [skip ci] ([d13321b](https://github.com/VinciGit00/Scrapegraph-ai/commit/d13321b2f86d98e2a3a0c563172ca0dd29cdf5fb))
* **release:** 0.5.0-beta.1 [skip ci] ([450291f](https://github.com/VinciGit00/Scrapegraph-ai/commit/450291f52e48cd35b2b8cc50ff66f5336326fa25))
* **release:** 0.5.0-beta.2 [skip ci] ([ff7d12f](https://github.com/VinciGit00/Scrapegraph-ai/commit/ff7d12f1389d8eed87e9f6b2fc8b099767a904a9))
* **release:** 0.5.0-beta.3 [skip ci] ([7e81f7c](https://github.com/VinciGit00/Scrapegraph-ai/commit/7e81f7c03f79c43219743be52affabbaf0d66387))
* **release:** 0.5.0-beta.4 [skip ci] ([14e56f6](https://github.com/VinciGit00/Scrapegraph-ai/commit/14e56f6ab1711a08e749edbda860d349db491dae))
* **release:** 0.5.0-beta.5 [skip ci] ([5ac97e2](https://github.com/VinciGit00/Scrapegraph-ai/commit/5ac97e2fb321be40c9787fbf8cb53fa62cf0ce06))
* **release:** 0.5.0-beta.6 [skip ci] ([9356124](https://github.com/VinciGit00/Scrapegraph-ai/commit/9356124ce39568e88f7d2965181579c4ff0a5752))


## [0.5.0-beta.6](https://github.com/VinciGit00/Scrapegraph-ai/compare/v0.5.0-beta.5...v0.5.0-beta.6) (2024-04-30)


### Features

* added verbose flag to suppress print statements ([2dd7817](https://github.com/VinciGit00/Scrapegraph-ai/commit/2dd7817cfb37cfbeb7e65b3a24655ab238f48026))

## [0.5.0-beta.5](https://github.com/VinciGit00/Scrapegraph-ai/compare/v0.5.0-beta.4...v0.5.0-beta.5) (2024-04-30)


### Features

* **refactor:** changed variable names ([8fba7e5](https://github.com/VinciGit00/Scrapegraph-ai/commit/8fba7e5490f916b325588443bba3fff5c0733c17))

## [0.5.0-beta.4](https://github.com/VinciGit00/Scrapegraph-ai/compare/v0.5.0-beta.3...v0.5.0-beta.4) (2024-04-30)


### Bug Fixes

* script generator and add new benchmarks ([e3d0194](https://github.com/VinciGit00/Scrapegraph-ai/commit/e3d0194dc93b20dc254fc48bba11559bf8a3a185))

## [0.5.0-beta.3](https://github.com/VinciGit00/Scrapegraph-ai/compare/v0.5.0-beta.2...v0.5.0-beta.3) (2024-04-30)


### Features

* add cluade integration ([e0ffc83](https://github.com/VinciGit00/Scrapegraph-ai/commit/e0ffc838b06c0f024026a275fc7f7b4243ad5cf9))

## [0.5.0-beta.2](https://github.com/VinciGit00/Scrapegraph-ai/compare/v0.5.0-beta.1...v0.5.0-beta.2) (2024-04-30)


### Features

* **fetch:** added playwright support ([42ab0aa](https://github.com/VinciGit00/Scrapegraph-ai/commit/42ab0aa1d275b5798ab6fc9feea575fe59b6e767))

## [0.5.0-beta.1](https://github.com/VinciGit00/Scrapegraph-ai/compare/v0.4.1...v0.5.0-beta.1) (2024-04-30)


### Features

* add co-author ([719a353](https://github.com/VinciGit00/Scrapegraph-ai/commit/719a353410992cc96f46ec984a5d3ec372e71ad2))
* base groq + requirements + toml update with groq ([7dd5b1a](https://github.com/VinciGit00/Scrapegraph-ai/commit/7dd5b1a03327750ffa5b2fb647eda6359edd1fc2))
* **llm:** implemented groq model ([dbbf10f](https://github.com/VinciGit00/Scrapegraph-ai/commit/dbbf10fc77b34d99d64c6cd7f74524b6d8e57fa5))
* updated requirements.txt ([d368725](https://github.com/VinciGit00/Scrapegraph-ai/commit/d36872518a6d234eba5f8b7ddca7da93797874b2))


### CI

* **release:** 0.4.0-beta.3 [skip ci] ([d13321b](https://github.com/VinciGit00/Scrapegraph-ai/commit/d13321b2f86d98e2a3a0c563172ca0dd29cdf5fb))

## [0.4.1](https://github.com/VinciGit00/Scrapegraph-ai/compare/v0.4.0...v0.4.1) (2024-04-28)



### Bug Fixes


* added missing dependecies ([7f1c3b7](https://github.com/VinciGit00/Scrapegraph-ai/commit/7f1c3b7d833ac782da17829dc021e86e258cf461))

## [0.4.0](https://github.com/VinciGit00/Scrapegraph-ai/compare/v0.3.0...v0.4.0) (2024-04-28)


### Features

* add new proxy rotation function ([f6077d1](https://github.com/VinciGit00/Scrapegraph-ai/commit/f6077d1f98023ac3bf0c89ef6b3d67dde4818df7))


### Bug Fixes

* bug for calculate costs ([a9b11e4](https://github.com/VinciGit00/Scrapegraph-ai/commit/a9b11e433a28dc111bce260d6a83849410fcb03c))
* bug with fetch node ([9cd5165](https://github.com/VinciGit00/Scrapegraph-ai/commit/9cd516507cc5ad65b100522b488cb0272dc7b366))
* changed proxy function ([b754dd9](https://github.com/VinciGit00/Scrapegraph-ai/commit/b754dd909cd2aa2d5b5d94d9c7879ba3da58adc4))
* robot node and proxyes ([adbc08f](https://github.com/VinciGit00/Scrapegraph-ai/commit/adbc08f27bc0966822f054f3af0e1f94fc0b87f5))


### CI

* **release:** 0.4.0-beta.1 [skip ci] ([4bc7274](https://github.com/VinciGit00/Scrapegraph-ai/commit/4bc727412f3b329491300ae2efb705a8386801d2))
* **release:** 0.4.0-beta.2 [skip ci] ([3c77acb](https://github.com/VinciGit00/Scrapegraph-ai/commit/3c77acbb1de43b8b09b5f46e69e38f9fa5551120))


## [0.4.0-beta.2](https://github.com/VinciGit00/Scrapegraph-ai/compare/v0.4.0-beta.1...v0.4.0-beta.2) (2024-04-27)


### Bug Fixes

* robot node and proxyes ([adbc08f](https://github.com/VinciGit00/Scrapegraph-ai/commit/adbc08f27bc0966822f054f3af0e1f94fc0b87f5))

## [0.4.0-beta.1](https://github.com/VinciGit00/Scrapegraph-ai/compare/v0.3.0...v0.4.0-beta.1) (2024-04-27)


### Features

* add new proxy rotation function ([f6077d1](https://github.com/VinciGit00/Scrapegraph-ai/commit/f6077d1f98023ac3bf0c89ef6b3d67dde4818df7))


### Bug Fixes

* changed proxy function ([b754dd9](https://github.com/VinciGit00/Scrapegraph-ai/commit/b754dd909cd2aa2d5b5d94d9c7879ba3da58adc4))

## [0.3.0](https://github.com/VinciGit00/Scrapegraph-ai/compare/v0.2.8...v0.3.0) (2024-04-26)


### Features

* trigger new beta release ([26c92c3](https://github.com/VinciGit00/Scrapegraph-ai/commit/26c92c3969b9a3149d6a16ea4a623a2041b97483))
* trigger new beta release ([6f028c4](https://github.com/VinciGit00/Scrapegraph-ai/commit/6f028c499342655851044f54de2a8cc1b9b95697))


### CI

* **release:** 0.3.0-beta.1 [skip ci] ([b481fd7](https://github.com/VinciGit00/Scrapegraph-ai/commit/b481fd7602dc6b9bdc2644a10ad24981c602efd7))
* **release:** 0.3.0-beta.2 [skip ci] ([7c8dbb8](https://github.com/VinciGit00/Scrapegraph-ai/commit/7c8dbb8ac1f35315abd2740c561d70edf4a8262d))
* add ci workflow to manage lib release with semantic-release ([92cd040](https://github.com/VinciGit00/Scrapegraph-ai/commit/92cd040dad8ba91a22515f3845f8dbb5f6a6939c))
* remove pull request trigger and fix plugin release train ([876fe66](https://github.com/VinciGit00/Scrapegraph-ai/commit/876fe668d97adef3863446836b10a3c00a2eb82d))

## [0.3.0-beta.2](https://github.com/VinciGit00/Scrapegraph-ai/compare/v0.3.0-beta.1...v0.3.0-beta.2) (2024-04-26)


### Features

* trigger new beta release ([26c92c3](https://github.com/VinciGit00/Scrapegraph-ai/commit/26c92c3969b9a3149d6a16ea4a623a2041b97483))

## [0.3.0-beta.1](https://github.com/VinciGit00/Scrapegraph-ai/compare/v0.2.8...v0.3.0-beta.1) (2024-04-26)


### Features

* trigger new beta release ([6f028c4](https://github.com/VinciGit00/Scrapegraph-ai/commit/6f028c499342655851044f54de2a8cc1b9b95697))


### CI

* add ci workflow to manage lib release with semantic-release ([92cd040](https://github.com/VinciGit00/Scrapegraph-ai/commit/92cd040dad8ba91a22515f3845f8dbb5f6a6939c))
* remove pull request trigger and fix plugin release train ([876fe66](https://github.com/VinciGit00/Scrapegraph-ai/commit/876fe668d97adef3863446836b10a3c00a2eb82d))
