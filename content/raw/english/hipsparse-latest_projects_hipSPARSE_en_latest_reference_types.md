---
title: "hipSPARSE data types &#8212; hipSPARSE 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipSPARSE/en/latest/reference/types.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:09:39.449569+00:00
content_hash: "a609ed8559b2823e"
---

# hipSPARSE data types[#](#hipsparse-data-types)

## hipsparseHandle_t[#](#hipsparsehandle-t)

-
typedef void *hipsparseHandle_t
[#](#_CPPv417hipsparseHandle_t) Handle to the hipSPARSE library context queue.

The hipSPARSE handle is a structure holding the hipSPARSE library context. It must be initialized using

[hipsparseCreate()](auxiliary.html#hipsparse-auxiliary_8h_1a3c9c4b579d7adab6fc8304e8437ffaec)and the returned handle must be passed to all subsequent library function calls. It should be destroyed at the end using[hipsparseDestroy()](auxiliary.html#hipsparse-auxiliary_8h_1a320899e020b6f66f73730105f0ad98c0).

## hipsparseMatDescr_t[#](#hipsparsematdescr-t)

-
typedef void *hipsparseMatDescr_t
[#](#_CPPv419hipsparseMatDescr_t) Descriptor of the matrix.

The hipSPARSE matrix descriptor is a structure holding all properties of a matrix. It must be initialized using

[hipsparseCreateMatDescr()](auxiliary.html#hipsparse-auxiliary_8h_1ad59af5607dfcc075c302b79febaa382b)and the returned descriptor must be passed to all subsequent library calls that involve the matrix. It should be destroyed at the end using[hipsparseDestroyMatDescr()](auxiliary.html#hipsparse-auxiliary_8h_1a21684bd690594fd8f98718eb3094f30b).

## hipsparseHybMat_t[#](#hipsparsehybmat-t)

-
typedef void *hipsparseHybMat_t
[#](#_CPPv417hipsparseHybMat_t) HYB matrix storage format.

The hipSPARSE HYB matrix structure holds the HYB matrix. It must be initialized using

[hipsparseCreateHybMat()](auxiliary.html#hipsparse-auxiliary_8h_1ab0a4ae83034f87cff9c9405150261648)and the returned HYB matrix must be passed to all subsequent library calls that involve the matrix. It should be destroyed at the end using[hipsparseDestroyHybMat()](auxiliary.html#hipsparse-auxiliary_8h_1a1e97ab0183146de9e21d9dd8333d0a18).

For more details on the HYB format, see [HYB storage format](../howto/using-hipsparse.html#hyb-storage-format).

## hipsparseColorInfo_t[#](#hipsparsecolorinfo-t)

-
typedef void *hipsparseColorInfo_t
[#](#_CPPv420hipsparseColorInfo_t) Pointer type to opaque structure holding coloring info.

The hipSPARSE ColorInfo structure holds the coloring information. It must be initialized using

[hipsparseCreateColorInfo()](auxiliary.html#hipsparse-auxiliary_8h_1a7bdb23d97ee767bed4f62a8d7f867b11)and the returned structure must be passed to all subsequent library calls that involve the coloring. It should be destroyed at the end using[hipsparseDestroyColorInfo()](auxiliary.html#hipsparse-auxiliary_8h_1a31e93a4d1e43a3bbc78ca0d04e9449c7).

## bsrsv2Info_t[#](#bsrsv2info-t)

-
typedef struct bsrsv2Info *bsrsv2Info_t
[#](#_CPPv412bsrsv2Info_t) Pointer type to opaque structure holding bsrsv2 info.

The hipSPARSE bsrsv2 structure holds the information used by

[hipsparseXbsrsv2_zeroPivot()](level2.html#hipsparse__bsrsv_8h_1a8772270c10f8bdfb033e0dbb7d74cd82),[hipsparseXbsrsv2_bufferSize()](level2.html#hipsparse__bsrsv_8h_1a83d97ea0c338ecf860e6292b5d7637dd),[hipsparseXbsrsv2_bufferSizeExt()](level2.html#hipsparse__bsrsv_8h_1ab17d7261565de97d2fc710075c63f18d),[hipsparseXbsrsv2_analysis()](level2.html#hipsparse__bsrsv_8h_1ac81adbb927bbccfc1627e3c0f36ea8bd), and[hipsparseXbsrsv2_solve()](level2.html#hipsparse__bsrsv_8h_1a7a6e7dac8f1cb43d92ea2df1f1e65c18). It must be initialized using[hipsparseCreateBsrsv2Info()](auxiliary.html#hipsparse-auxiliary_8h_1a8344d2fac58a157318afdb50dea4e798)and the returned structure must be passed to all subsequent library calls that involve bsrsv2. It should be destroyed at the end using[hipsparseDestroyBsrsv2Info()](auxiliary.html#hipsparse-auxiliary_8h_1a841ac0ec43568a501db3fb2b656fff1b).

## bsrsm2Info_t[#](#bsrsm2info-t)

-
typedef struct bsrsm2Info *bsrsm2Info_t
[#](#_CPPv412bsrsm2Info_t) Pointer type to opaque structure holding bsrsm2 info.

The hipSPARSE bsrsm2 structure holds the information used by

[hipsparseXbsrsm2_zeroPivot()](level3.html#hipsparse__bsrsm_8h_1a6d4fd566a8037938f5d3929208b848cd),[hipsparseXbsrsm2_bufferSize()](level3.html#hipsparse__bsrsm_8h_1afc00f788090e6c16c1e790b9683df3b8),[hipsparseXbsrsm2_analysis()](level3.html#hipsparse__bsrsm_8h_1aacd9b432867bd4ef875955696c57ccd4), and[hipsparseXbsrsm2_solve()](level3.html#hipsparse__bsrsm_8h_1a5103145304428e88b9ccb189c6a5a790). It must be initialized using[hipsparseCreateBsrsm2Info()](auxiliary.html#hipsparse-auxiliary_8h_1aaac20be8fc49ef327f0acb7cfac2d801)and the returned structure must be passed to all subsequent library calls that involve bsrsm2. It should be destroyed at the end using[hipsparseDestroyBsrsm2Info()](auxiliary.html#hipsparse-auxiliary_8h_1a63ffdc1ecd67733ae40fe04d6889502d).

## bsrilu02Info_t[#](#bsrilu02info-t)

-
typedef struct bsrilu02Info *bsrilu02Info_t
[#](#_CPPv414bsrilu02Info_t) Pointer type to opaque structure holding bsrilu02 info.

The hipSPARSE bsrilu02 structure holds the information used by

[hipsparseXbsrilu02_zeroPivot()](precond.html#hipsparse__bsrilu0_8h_1a53831a4fbf7559ddd3efed860ff8e79f),[hipsparseXbsrilu02_numericBoost()](precond.html#hipsparse__bsrilu0_8h_1a7ce1bed8b12b7501b9aa34d56e7ac0ef),[hipsparseXbsrilu02_bufferSize()](precond.html#hipsparse__bsrilu0_8h_1a8efe2b2ba788104b397bbe5ab75cce8d),[hipsparseXbsrilu02_analysis()](precond.html#hipsparse__bsrilu0_8h_1a47d4addbbfeb087b1050a3b1a6c11b56), and[hipsparseXbsrilu02()](precond.html#hipsparse__bsrilu0_8h_1a79aa95847c1439cba4250be3ac0460e3). It must be initialized using[hipsparseCreateBsrilu02Info()](auxiliary.html#hipsparse-auxiliary_8h_1a53c47303bb24fcca768d658ed207df73)and the returned structure must be passed to all subsequent library calls that involve bsrilu02. It should be destroyed at the end using[hipsparseDestroyBsrilu02Info()](auxiliary.html#hipsparse-auxiliary_8h_1ab33fdae0197dd03f61d4c5fd8e278bac).

## bsric02Info_t[#](#bsric02info-t)

-
typedef struct bsric02Info *bsric02Info_t
[#](#_CPPv413bsric02Info_t) Pointer type to opaque structure holding bsric02 info.

The hipSPARSE bsric02 structure holds the information used by

[hipsparseXbsric02_zeroPivot()](precond.html#hipsparse__bsric0_8h_1a4f2a00c9180b635f14c0c7d33cc5a408),[hipsparseXbsric02_bufferSize()](precond.html#hipsparse__bsric0_8h_1a9573e196c9f4eacc5cf2e44a25e817d1),[hipsparseXbsric02_analysis()](precond.html#hipsparse__bsric0_8h_1a3f330948f32374685ad4cf062ed51af8), and[hipsparseXbsric02()](precond.html#hipsparse__bsric0_8h_1a3b4e7c01e4bb25b62c05b90a5d1307e1). It must be initialized using[hipsparseCreateBsric02Info()](auxiliary.html#hipsparse-auxiliary_8h_1ae6c20695709c3eb97e11b973f01eeb0c)and the returned structure must be passed to all subsequent library calls that involve bsric02. It should be destroyed at the end using[hipsparseDestroyBsric02Info()](auxiliary.html#hipsparse-auxiliary_8h_1a2554df520ef427bd99c38414df1324ee).

## csrsv2Info_t[#](#csrsv2info-t)

-
typedef struct csrsv2Info *csrsv2Info_t
[#](#_CPPv412csrsv2Info_t) Pointer type to opaque structure holding csrsv2 info.

The hipSPARSE csrsv2 structure holds the information used by

[hipsparseXcsrsv2_zeroPivot()](level2.html#hipsparse__csrsv_8h_1a12b4fe69770b7a69609a1f54ab3869b5),[hipsparseXcsrsv2_bufferSize()](level2.html#hipsparse__csrsv_8h_1ac2b333394fd5c3ed2c1cf717bf2d1661),[hipsparseXcsrsv2_analysis()](level2.html#hipsparse__csrsv_8h_1a201995e83a6140db524e3b15cbed4dcb), and[hipsparseXcsrsv2_solve()](level2.html#hipsparse__csrsv_8h_1ae696c633b40b43ea9c3b9bc1387db731). It must be initialized using[hipsparseCreateCsrsv2Info()](auxiliary.html#hipsparse-auxiliary_8h_1a07237c8ee721f51aaeb07477bcac61a4)and the returned structure must be passed to all subsequent library calls that involve csrsv2. It should be destroyed at the end using[hipsparseDestroyCsrsv2Info()](auxiliary.html#hipsparse-auxiliary_8h_1a2aade2ef1590036d61764e52bd4d1b05).

## csrsm2Info_t[#](#csrsm2info-t)

-
typedef struct csrsm2Info *csrsm2Info_t
[#](#_CPPv412csrsm2Info_t) Pointer type to opaque structure holding csrsm2 info.

The hipSPARSE csrsm2 structure holds the information used by

[hipsparseXcsrsm2_zeroPivot()](level3.html#hipsparse__csrsm_8h_1a0ea9dd8a24b17270fde9ddbaed87c54d),[hipsparseXcsrsm2_bufferSizeExt()](level3.html#hipsparse__csrsm_8h_1a36c0b1981e97635cde38cf9fcbbc37ac),[hipsparseXcsrsm2_analysis()](level3.html#hipsparse__csrsm_8h_1aec706e7d801804490c7609b6796ddf0f), and[hipsparseXcsrsm2_solve()](level3.html#hipsparse__csrsm_8h_1a410914eb84ccae282c09b6022351422a). It must be initialized using[hipsparseCreateCsrsm2Info()](auxiliary.html#hipsparse-auxiliary_8h_1aefa902d63e2d5c3a4673a876da7c4312)and the returned structure must be passed to all subsequent library calls that involve csrsm2. It should be destroyed at the end using[hipsparseDestroyCsrsm2Info()](auxiliary.html#hipsparse-auxiliary_8h_1a54ce02e38d0514887788ac6964a21f1e).

## csrilu02Info_t[#](#csrilu02info-t)

-
typedef struct csrilu02Info *csrilu02Info_t
[#](#_CPPv414csrilu02Info_t) Pointer type to opaque structure holding csrilu02 info.

The hipSPARSE csrilu02 structure holds the information used by

[hipsparseXcsrilu02_zeroPivot()](precond.html#hipsparse__csrilu0_8h_1ab139ea359b40dd01937f8cd6f6890d04),[hipsparseXcsrilu02_numericBoost()](precond.html#hipsparse__csrilu0_8h_1aa93aa881485b02febb2e2d4d8145e84c),[hipsparseXcsrilu02_bufferSize()](precond.html#hipsparse__csrilu0_8h_1a1cdc19abd5d4d3defb3737c790f8f010),[hipsparseXcsrilu02_analysis()](precond.html#hipsparse__csrilu0_8h_1af9373f20b711d53705ac27a3a12ff894), and[hipsparseXcsrilu02()](precond.html#hipsparse__csrilu0_8h_1a7fd68be2e8b248a9ee7304b24d3819a0). It must be initialized using[hipsparseCreateCsrilu02Info()](auxiliary.html#hipsparse-auxiliary_8h_1a9fd2a76eb2b49c15a8a47872fedfa7ca)and the returned structure must be passed to all subsequent library calls that involve csrilu02. It should be destroyed at the end using[hipsparseDestroyCsrilu02Info()](auxiliary.html#hipsparse-auxiliary_8h_1ada7faf2216e4bf9a4b2b37f8b621b343).

## csric02Info_t[#](#csric02info-t)

-
typedef struct csric02Info *csric02Info_t
[#](#_CPPv413csric02Info_t) Pointer type to opaque structure holding csric02 info.

The hipSPARSE csric02 structure holds the information used by

[hipsparseXcsric02_zeroPivot()](precond.html#hipsparse__csric0_8h_1a8400c63b72d75beae59167a0e790eac2),[hipsparseXcsric02_bufferSize()](precond.html#hipsparse__csric0_8h_1ae324850728daf314b0f24bd9376cb91d),[hipsparseXcsric02_analysis()](precond.html#hipsparse__csric0_8h_1a047d0b5927a32cbeef5ea061ef89a4b4), and[hipsparseXcsric02()](precond.html#hipsparse__csric0_8h_1a59983f16d2c4bcf1fe265b4ba25b29a3). It must be initialized using[hipsparseCreateCsric02Info()](auxiliary.html#hipsparse-auxiliary_8h_1aaca9f87533c49640541b42eb803e1bb9)and the returned structure must be passed to all subsequent library calls that involve csric02. It should be destroyed at the end using[hipsparseDestroyCsric02Info()](auxiliary.html#hipsparse-auxiliary_8h_1a656fa4a86918b2f33db754aec7c692f9).

## csrgemm2Info_t[#](#csrgemm2info-t)

-
typedef struct csrgemm2Info *csrgemm2Info_t
[#](#_CPPv414csrgemm2Info_t) Pointer type to opaque structure holding csrgemm2 info.

The hipSPARSE csrgemm2 structure holds the information used by

[hipsparseXcsrgemm2_bufferSizeExt()](extra.html#hipsparse__csrgemm_8h_1a9f570232697e2acfacd584ea74513db1),[hipsparseXcsrgemm2Nnz()](extra.html#hipsparse__csrgemm_8h_1a6a9ad055ef2698ae82a819363e2be0fa), and[hipsparseXcsrgemm2()](extra.html#hipsparse__csrgemm_8h_1a3cd3c5f29897ec4ad5ba0512cd4b6d47). It must be initialized using[hipsparseCreateCsrgemm2Info()](auxiliary.html#hipsparse-auxiliary_8h_1ae90de387125fa4acb5eec19eb2d92080)and the returned structure must be passed to all subsequent library calls that involve csrgemm2. It should be destroyed at the end using[hipsparseDestroyCsrgemm2Info()](auxiliary.html#hipsparse-auxiliary_8h_1a853e11e6f0282141bdb3957813f752f4).

## pruneInfo_t[#](#pruneinfo-t)

-
typedef struct pruneInfo *pruneInfo_t
[#](#_CPPv411pruneInfo_t) Pointer type to opaque structure holding prune info.

The hipSPARSE prune structure holds the information used by

[hipsparseXpruneDense2csrByPercentage_bufferSize()](conversion.html#hipsparse__prune__dense2csr__by__percentage_8h_1afe90279b2f19fceb880883e98156e29e),[hipsparseXpruneDense2csrByPercentage_bufferSizeExt()](conversion.html#hipsparse__prune__dense2csr__by__percentage_8h_1a5f59e4f1ade1b8b383cc39e7adf7da58),[hipsparseXpruneCsr2csrByPercentage_bufferSize()](conversion.html#hipsparse__prune__csr2csr__by__percentage_8h_1a7a3cc1745b789370fb69d3068c9dd925),[hipsparseXpruneCsr2csrByPercentage_bufferSizeExt()](conversion.html#hipsparse__prune__csr2csr__by__percentage_8h_1aa37709e126490b8485f051739c0e4542),[hipsparseXpruneDense2csrNnzByPercentage()](conversion.html#hipsparse__prune__dense2csr__by__percentage_8h_1afa03216a28f5bf36e3bce51950b4a140),[hipsparseXpruneCsr2csrNnzByPercentage()](conversion.html#hipsparse__prune__csr2csr__by__percentage_8h_1a49fdcbf9234f1ca31b1260183ffe49d7),[hipsparseXpruneDense2csrByPercentage()](conversion.html#hipsparse__prune__dense2csr__by__percentage_8h_1ace1c36935b6211e53445f81331cc190b), and[hipsparseXpruneCsr2csrByPercentage()](conversion.html#hipsparse__prune__csr2csr__by__percentage_8h_1aec7357dd8820e2aaf5aefce1c045a772). It must be initialized using[hipsparseCreatePruneInfo()](auxiliary.html#hipsparse-auxiliary_8h_1a1420f8823529bbc5a277505abb5be406)and the returned structure must be passed to all subsequent library calls that involve prune. It should be destroyed at the end using[hipsparseDestroyPruneInfo()](auxiliary.html#hipsparse-auxiliary_8h_1ab497109423846bc1c4325a4e4a9d7b21).

## csru2csrInfo_t[#](#csru2csrinfo-t)

-
typedef struct csru2csrInfo *csru2csrInfo_t
[#](#_CPPv414csru2csrInfo_t) Pointer type to opaque structure holding csru2csr info.

The hipSPARSE csru2csr structure holds the information used by

[hipsparseXcsru2csr_bufferSizeExt()](conversion.html#hipsparse__csru2csr_8h_1a1b41b016db89d6677cedb243de2d9d3e),[hipsparseXcsru2csr()](conversion.html#hipsparse__csru2csr_8h_1a9b88ff52694f00c9f853bb67b683efe2), and[hipsparseXcsr2csru()](conversion.html#hipsparse__csr2csru_8h_1a9dce04506d41073596ba5f34ef535597). It must be initialized using[hipsparseCreateCsru2csrInfo()](auxiliary.html#hipsparse-auxiliary_8h_1aed8c291a06ca15f75d0d043503dec50e)and the returned structure must be passed to all subsequent library calls that involve csru2csr. It should be destroyed at the end using[hipsparseDestroyCsru2csrInfo()](auxiliary.html#hipsparse-auxiliary_8h_1a910c7704054c8e51ea819af184a70abf).

## hipsparseSpVecDescr_t[#](#hipsparsespvecdescr-t)

-
typedef void *hipsparseSpVecDescr_t
[#](#_CPPv421hipsparseSpVecDescr_t) Generic API opaque structure holding information for a sparse vector.

The hipSPARSE descriptor is an opaque structure holding information for a sparse vector. It must be initialized using

[hipsparseCreateSpVec()](auxiliary.html#hipsparse-generic-auxiliary_8h_1a13a0e16b493f904bfe7a100e95309ff6)and the returned descriptor is used in hipSPARSE generic API’s involving sparse vectors. It should be destroyed at the end using[hipsparseDestroySpVec()](auxiliary.html#hipsparse-generic-auxiliary_8h_1ac833153c10c06c6e349c5b11c6a9a549).

## hipsparseSpMatDescr_t[#](#hipsparsespmatdescr-t)

-
typedef struct hipsparseSpMatDescr_st *hipsparseSpMatDescr_t
[#](#_CPPv421hipsparseSpMatDescr_t) Generic API opaque structure holding information for a sparse matrix.

The hipSPARSE descriptor is an opaque structure holding information for a sparse matrix. It must be initialized using either

[hipsparseCreateCoo()](auxiliary.html#hipsparse-generic-auxiliary_8h_1ab9de2e90db2834ccbf1e52fb7c47df64)(for COO format),[hipsparseCreateCooAoS()](auxiliary.html#hipsparse-generic-auxiliary_8h_1a9c9a35dff79601aed1df828171ff9eee)(for COO AOS format).[hipsparseCreateCsr()](auxiliary.html#hipsparse-generic-auxiliary_8h_1a86683ee73eaa728ae7bd9e328223f473)(for CSR format),[hipsparseCreateCsc()](auxiliary.html#hipsparse-generic-auxiliary_8h_1a05b8b74f37a73c5ed5cfd3dc67b67494)(for CSC format) or[hipsparseCreateBlockedEll()](auxiliary.html#hipsparse-generic-auxiliary_8h_1a8a4dbf88c8f0bfca2d3245bf9b15a412)(for Blocked ELL format). The returned descriptor is used in hipSPARSE generic API’s involving sparse matrices. It should be destroyed at the end using[hipsparseDestroySpMat()](auxiliary.html#hipsparse-generic-auxiliary_8h_1a667c7b0eb0d50b4ff95cac5130615726).

## hipsparseDnVecDescr_t[#](#hipsparsednvecdescr-t)

-
typedef void *hipsparseDnVecDescr_t
[#](#_CPPv421hipsparseDnVecDescr_t) Generic API opaque structure holding information for a dense vector.

The hipSPARSE descriptor is an opaque structure holding information for a dense vector. It must be initialized using

[hipsparseCreateDnVec()](auxiliary.html#hipsparse-generic-auxiliary_8h_1a408d052a674940b5ce5f075d24e8a751)and the returned descriptor is used in hipSPARSE generic API’s involving dense vectors. It should be destroyed at the end using[hipsparseDestroyDnVec()](auxiliary.html#hipsparse-generic-auxiliary_8h_1abe2ba87d1ba1ba7d4ca2e6af0c870565).

## hipsparseDnMatDescr_t[#](#hipsparsednmatdescr-t)

-
typedef void *hipsparseDnMatDescr_t
[#](#_CPPv421hipsparseDnMatDescr_t) Generic API opaque structure holding information for a dense matrix.

The hipSPARSE descriptor is an opaque structure holding information for a dense matrix. It must be initialized using

[hipsparseCreateDnMat()](auxiliary.html#hipsparse-generic-auxiliary_8h_1aa037b981d507f50e241dffc5e118a543)and the returned descriptor is used in hipSPARSE generic API’s involving dense matrices. It should be destroyed at the end using[hipsparseDestroyDnMat()](auxiliary.html#hipsparse-generic-auxiliary_8h_1ab364f0605fcb79337045a7782cadaaec).

## hipsparseSpGEMMDescr_t[#](#hipsparsespgemmdescr-t)

-
typedef struct hipsparseSpGEMMDescr *hipsparseSpGEMMDescr_t
[#](#_CPPv422hipsparseSpGEMMDescr_t) Generic API opaque structure holding information for a SpGEMM calculations.

The hipSPARSE descriptor is an opaque structure holding information that is used in

[hipsparseSpGEMM_workEstimation()](generic.html#hipsparse__spgemm_8h_1a07931f15e3ab3b1303c9d55b692cb4b1),[hipsparseSpGEMMreuse_workEstimation()](generic.html#hipsparse__spgemm__reuse_8h_1a511d08f0e0ac2eaf9ca72872d0a1aaa8),[hipsparseSpGEMMreuse_nnz()](generic.html#hipsparse__spgemm__reuse_8h_1ad4cbe0f6b03420530f350a1165b584dd),[hipsparseSpGEMM_compute()](generic.html#hipsparse__spgemm_8h_1a4fa64f7cfd9d47276c832490aa0f1251),[hipsparseSpGEMMreuse_compute()](generic.html#hipsparse__spgemm__reuse_8h_1a52651a4a513d513f9ccc23d516c70823),[hipsparseSpGEMM_copy()](generic.html#hipsparse__spgemm_8h_1a299610cce161dd7ebb36dcc83a6d068d), and[hipsparseSpGEMMreuse_copy()](generic.html#hipsparse__spgemm__reuse_8h_1a9a9a76c118844cd6279f64b7ca95956b). It must be initialized using[hipsparseSpGEMM_createDescr()](generic.html#hipsparse__spgemm_8h_1a5394a448e4c20bc1135cbfbf09ee3bb0). It should be destroyed at the end using[hipsparseSpGEMM_destroyDescr()](generic.html#hipsparse__spgemm_8h_1a539207acdf900526b27a20a9ca923773).

## hipsparseSpSVDescr_t[#](#hipsparsespsvdescr-t)

-
typedef struct hipsparseSpSVDescr *hipsparseSpSVDescr_t
[#](#_CPPv420hipsparseSpSVDescr_t) Generic API opaque structure holding information for a SpSV calculations.

The hipSPARSE descriptor is an opaque structure holding information that is used in

[hipsparseSpSV_bufferSize()](generic.html#hipsparse__spsv_8h_1a6a47526261741c624acb9511cb70e669),[hipsparseSpSV_analysis()](generic.html#hipsparse__spsv_8h_1a22c011e445b2a217ab47ff1f7e84f25d), and[hipsparseSpSV_solve()](generic.html#hipsparse__spsv_8h_1a120f5f65677a69730ae7630b7027ee6c). It must be initialized using[hipsparseSpSV_createDescr()](generic.html#hipsparse__spsv_8h_1ac51c7a1a255af78106cc99a727f83112). It should be destroyed at the end using[hipsparseSpSV_destroyDescr()](generic.html#hipsparse__spsv_8h_1a1cec939dbc1a55370694da3f718f7dde).

## hipsparseSpSMDescr_t[#](#hipsparsespsmdescr-t)

-
typedef struct hipsparseSpSMDescr *hipsparseSpSMDescr_t
[#](#_CPPv420hipsparseSpSMDescr_t) Generic API opaque structure holding information for a SpSM calculations.

The hipSPARSE descriptor is an opaque structure holding information that is used in

[hipsparseSpSM_bufferSize()](generic.html#hipsparse__spsm_8h_1a162f0d8273e0fa5ff86b6a157c0e2a2d),[hipsparseSpSM_analysis()](generic.html#hipsparse__spsm_8h_1a64862dcaca88252ee31888b611a75380), and[hipsparseSpSM_solve()](generic.html#hipsparse__spsm_8h_1a1396f9876800f44cf5fca0c2efc524c0). It must be initialized using[hipsparseSpSM_createDescr()](generic.html#hipsparse__spsm_8h_1a079b87e8ab705504650e08dd7479d228). It should be destroyed at the end using[hipsparseSpSM_destroyDescr()](generic.html#hipsparse__spsm_8h_1aa52c5c27bf7a6451282da2c26a32aae4).

## hipsparseStatus_t[#](#hipsparsestatus-t)

-
enum hipsparseStatus_t
[#](#_CPPv417hipsparseStatus_t) List of hipsparse status codes definition.

This is a list of the

[hipsparseStatus_t](#hipsparse-types_8h_1aa069bec7a4f24d00dab1dc4612d4de79)types that are used by the hipSPARSE library.*Values:*-
enumerator HIPSPARSE_STATUS_SUCCESS
[#](#_CPPv4N17hipsparseStatus_t24HIPSPARSE_STATUS_SUCCESSE) Function succeeds


-
enumerator HIPSPARSE_STATUS_NOT_INITIALIZED
[#](#_CPPv4N17hipsparseStatus_t32HIPSPARSE_STATUS_NOT_INITIALIZEDE) hipSPARSE was not initialized


-
enumerator HIPSPARSE_STATUS_ALLOC_FAILED
[#](#_CPPv4N17hipsparseStatus_t29HIPSPARSE_STATUS_ALLOC_FAILEDE) Resource allocation failed


-
enumerator HIPSPARSE_STATUS_INVALID_VALUE
[#](#_CPPv4N17hipsparseStatus_t30HIPSPARSE_STATUS_INVALID_VALUEE) Unsupported value was passed to the function


-
enumerator HIPSPARSE_STATUS_ARCH_MISMATCH
[#](#_CPPv4N17hipsparseStatus_t30HIPSPARSE_STATUS_ARCH_MISMATCHE) Device architecture not supported


-
enumerator HIPSPARSE_STATUS_MAPPING_ERROR
[#](#_CPPv4N17hipsparseStatus_t30HIPSPARSE_STATUS_MAPPING_ERRORE) Access to GPU memory space failed


-
enumerator HIPSPARSE_STATUS_EXECUTION_FAILED
[#](#_CPPv4N17hipsparseStatus_t33HIPSPARSE_STATUS_EXECUTION_FAILEDE) GPU program failed to execute


-
enumerator HIPSPARSE_STATUS_INTERNAL_ERROR
[#](#_CPPv4N17hipsparseStatus_t31HIPSPARSE_STATUS_INTERNAL_ERRORE) An internal hipSPARSE operation failed


-
enumerator HIPSPARSE_STATUS_MATRIX_TYPE_NOT_SUPPORTED
[#](#_CPPv4N17hipsparseStatus_t42HIPSPARSE_STATUS_MATRIX_TYPE_NOT_SUPPORTEDE) Matrix type not supported


-
enumerator HIPSPARSE_STATUS_ZERO_PIVOT
[#](#_CPPv4N17hipsparseStatus_t27HIPSPARSE_STATUS_ZERO_PIVOTE) Zero pivot was computed


-
enumerator HIPSPARSE_STATUS_NOT_SUPPORTED
[#](#_CPPv4N17hipsparseStatus_t30HIPSPARSE_STATUS_NOT_SUPPORTEDE) Operation is not supported


-
enumerator HIPSPARSE_STATUS_INSUFFICIENT_RESOURCES
[#](#_CPPv4N17hipsparseStatus_t39HIPSPARSE_STATUS_INSUFFICIENT_RESOURCESE) Resources are insufficient


-
enumerator HIPSPARSE_STATUS_SUCCESS

## hipsparsePointerMode_t[#](#hipsparsepointermode-t)

-
enum hipsparsePointerMode_t
[#](#_CPPv422hipsparsePointerMode_t) Indicates if the pointer is device pointer or host pointer.

The

[hipsparsePointerMode_t](#hipsparse-types_8h_1a4aee6c92be9410c58c46d33cc4d14bc4)indicates whether scalar values are passed by reference on the host or device. The[hipsparsePointerMode_t](#hipsparse-types_8h_1a4aee6c92be9410c58c46d33cc4d14bc4)can be changed by[hipsparseSetPointerMode()](auxiliary.html#hipsparse-auxiliary_8h_1a7d876174f77e1f8f816781af1c3c667c). The currently used pointer mode can be obtained by[hipsparseGetPointerMode()](auxiliary.html#hipsparse-auxiliary_8h_1a43910f43a64ce8c79945cc9bfdf80b5e).*Values:*-
enumerator HIPSPARSE_POINTER_MODE_HOST
[#](#_CPPv4N22hipsparsePointerMode_t27HIPSPARSE_POINTER_MODE_HOSTE) Scalar pointers are in host memory


-
enumerator HIPSPARSE_POINTER_MODE_DEVICE
[#](#_CPPv4N22hipsparsePointerMode_t29HIPSPARSE_POINTER_MODE_DEVICEE) Scalar pointers are in device memory


-
enumerator HIPSPARSE_POINTER_MODE_HOST

## hipsparseAction_t[#](#hipsparseaction-t)

-
enum hipsparseAction_t
[#](#_CPPv417hipsparseAction_t) Specify where the operation is performed on.

The

[hipsparseAction_t](#hipsparse-types_8h_1a728aa53636cea88149e375bf26bdeb75)indicates whether the operation is performed on the full matrix, or only on the sparsity pattern of the matrix.*Values:*-
enumerator HIPSPARSE_ACTION_SYMBOLIC
[#](#_CPPv4N17hipsparseAction_t25HIPSPARSE_ACTION_SYMBOLICE) Operate only on indices


-
enumerator HIPSPARSE_ACTION_NUMERIC
[#](#_CPPv4N17hipsparseAction_t24HIPSPARSE_ACTION_NUMERICE) Operate on data and indices


-
enumerator HIPSPARSE_ACTION_SYMBOLIC

## hipsparseMatrixType_t[#](#hipsparsematrixtype-t)

-
enum hipsparseMatrixType_t
[#](#_CPPv421hipsparseMatrixType_t) Specify the matrix type.

The

[hipsparseMatrixType_t](#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)indices the type of a matrix. For a given[hipsparseMatDescr_t](#hipsparse-types_8h_1a4c2f3ad3f2057bffb1adf6a8256537b9), the[hipsparseMatrixType_t](#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)can be set using[hipsparseSetMatType()](auxiliary.html#hipsparse-auxiliary_8h_1a9e7e6c93637564982aa1e2eef70d86e8). The current[hipsparseMatrixType_t](#hipsparse-types_8h_1ae015bd5fad7b76c11b0486fcb3b49c8b)of a matrix can be obtained by[hipsparseGetMatType()](auxiliary.html#hipsparse-auxiliary_8h_1a6ff30343218f4ea85a1a91f1b1b4d035).*Values:*-
enumerator HIPSPARSE_MATRIX_TYPE_GENERAL
[#](#_CPPv4N21hipsparseMatrixType_t29HIPSPARSE_MATRIX_TYPE_GENERALE) General matrix type


-
enumerator HIPSPARSE_MATRIX_TYPE_SYMMETRIC
[#](#_CPPv4N21hipsparseMatrixType_t31HIPSPARSE_MATRIX_TYPE_SYMMETRICE) Symmetric matrix type


-
enumerator HIPSPARSE_MATRIX_TYPE_HERMITIAN
[#](#_CPPv4N21hipsparseMatrixType_t31HIPSPARSE_MATRIX_TYPE_HERMITIANE) Hermitian matrix type


-
enumerator HIPSPARSE_MATRIX_TYPE_TRIANGULAR
[#](#_CPPv4N21hipsparseMatrixType_t32HIPSPARSE_MATRIX_TYPE_TRIANGULARE) Triangular matrix type


-
enumerator HIPSPARSE_MATRIX_TYPE_GENERAL

## hipsparseFillMode_t[#](#hipsparsefillmode-t)

-
enum hipsparseFillMode_t
[#](#_CPPv419hipsparseFillMode_t) Specify the matrix fill mode.

The

[hipsparseFillMode_t](#hipsparse-types_8h_1ace47655e52ed1bb17309eda331c44332)indicates whether the lower or the upper part is stored in a sparse triangular matrix. For a given[hipsparseMatDescr_t](#hipsparse-types_8h_1a4c2f3ad3f2057bffb1adf6a8256537b9), the[hipsparseFillMode_t](#hipsparse-types_8h_1ace47655e52ed1bb17309eda331c44332)can be set using[hipsparseSetMatFillMode()](auxiliary.html#hipsparse-auxiliary_8h_1a01f8fb669bb7edb25e4fafd4dc87d531). The current[hipsparseFillMode_t](#hipsparse-types_8h_1ace47655e52ed1bb17309eda331c44332)of a matrix can be obtained by[hipsparseGetMatFillMode()](auxiliary.html#hipsparse-auxiliary_8h_1a099baa3839c6be5f4773f7b0c00ded1f).*Values:*-
enumerator HIPSPARSE_FILL_MODE_LOWER
[#](#_CPPv4N19hipsparseFillMode_t25HIPSPARSE_FILL_MODE_LOWERE) Lower triangular part is stored


-
enumerator HIPSPARSE_FILL_MODE_UPPER
[#](#_CPPv4N19hipsparseFillMode_t25HIPSPARSE_FILL_MODE_UPPERE) Upper triangular part is stored


-
enumerator HIPSPARSE_FILL_MODE_LOWER

## hipsparseDiagType_t[#](#hipsparsediagtype-t)

-
enum hipsparseDiagType_t
[#](#_CPPv419hipsparseDiagType_t) Indicates if the diagonal entries are unity.

The

[hipsparseDiagType_t](#hipsparse-types_8h_1a79e036b6c0680cb37e2aa53d3542a054)indicates whether the diagonal entries of a matrix are unity or not. If[HIPSPARSE_DIAG_TYPE_UNIT](#hipsparse-types_8h_1a79e036b6c0680cb37e2aa53d3542a054a532a9a4a4eaf63a967bfaac7f9936b39)is specified, all present diagonal values will be ignored. For a given[hipsparseMatDescr_t](#hipsparse-types_8h_1a4c2f3ad3f2057bffb1adf6a8256537b9), the[hipsparseDiagType_t](#hipsparse-types_8h_1a79e036b6c0680cb37e2aa53d3542a054)can be set using[hipsparseSetMatDiagType()](auxiliary.html#hipsparse-auxiliary_8h_1aec6fa039793196011f15cfb0b21c2b59). The current[hipsparseDiagType_t](#hipsparse-types_8h_1a79e036b6c0680cb37e2aa53d3542a054)of a matrix can be obtained by[hipsparseGetMatDiagType()](auxiliary.html#hipsparse-auxiliary_8h_1ae7bbcb4709320054dad07e7e4abe1298).*Values:*-
enumerator HIPSPARSE_DIAG_TYPE_NON_UNIT
[#](#_CPPv4N19hipsparseDiagType_t28HIPSPARSE_DIAG_TYPE_NON_UNITE) Diagonal entries are non-unity


-
enumerator HIPSPARSE_DIAG_TYPE_UNIT
[#](#_CPPv4N19hipsparseDiagType_t24HIPSPARSE_DIAG_TYPE_UNITE) Diagonal entries are unity


-
enumerator HIPSPARSE_DIAG_TYPE_NON_UNIT

## hipsparseIndexBase_t[#](#hipsparseindexbase-t)

-
enum hipsparseIndexBase_t
[#](#_CPPv420hipsparseIndexBase_t) Specify the matrix index base.

The

[hipsparseIndexBase_t](#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4)indicates the index base of the indices. For a given[hipsparseMatDescr_t](#hipsparse-types_8h_1a4c2f3ad3f2057bffb1adf6a8256537b9), the[hipsparseIndexBase_t](#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4)can be set using[hipsparseSetMatIndexBase()](auxiliary.html#hipsparse-auxiliary_8h_1a3c81b4bd7b1e9bb04a63a620f51dc2a8). The current[hipsparseIndexBase_t](#hipsparse-types_8h_1a4c75947dafab9437245e5f1a47cc3cb4)of a matrix can be obtained by[hipsparseGetMatIndexBase()](auxiliary.html#hipsparse-auxiliary_8h_1a165264c3fee1dec36d527420ec269d57).*Values:*-
enumerator HIPSPARSE_INDEX_BASE_ZERO
[#](#_CPPv4N20hipsparseIndexBase_t25HIPSPARSE_INDEX_BASE_ZEROE) Zero based indexing


-
enumerator HIPSPARSE_INDEX_BASE_ONE
[#](#_CPPv4N20hipsparseIndexBase_t24HIPSPARSE_INDEX_BASE_ONEE) One based indexing


-
enumerator HIPSPARSE_INDEX_BASE_ZERO

## hipsparseOperation_t[#](#hipsparseoperation-t)

-
enum hipsparseOperation_t
[#](#_CPPv420hipsparseOperation_t) Specify whether the matrix is to be transposed or not.

The

[hipsparseOperation_t](#hipsparse-types_8h_1ae3dea1ad3fa65167c8a7b1a06128d141)indicates the operation performed with the given matrix.*Values:*-
enumerator HIPSPARSE_OPERATION_NON_TRANSPOSE
[#](#_CPPv4N20hipsparseOperation_t33HIPSPARSE_OPERATION_NON_TRANSPOSEE) Operate with matrix


-
enumerator HIPSPARSE_OPERATION_TRANSPOSE
[#](#_CPPv4N20hipsparseOperation_t29HIPSPARSE_OPERATION_TRANSPOSEE) Operate with transpose


-
enumerator HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSE
[#](#_CPPv4N20hipsparseOperation_t39HIPSPARSE_OPERATION_CONJUGATE_TRANSPOSEE) Operate with conj. transpose


-
enumerator HIPSPARSE_OPERATION_NON_TRANSPOSE

## hipsparseHybPartition_t[#](#hipsparsehybpartition-t)

-
enum hipsparseHybPartition_t
[#](#_CPPv423hipsparseHybPartition_t) HYB matrix partitioning type.

The

[hipsparseHybPartition_t](#hipsparse-types_8h_1a982aa7c059922aafb1f77bfc868a460f)type indicates how the hybrid format partitioning between COO and ELL storage formats is performed.*Values:*-
enumerator HIPSPARSE_HYB_PARTITION_AUTO
[#](#_CPPv4N23hipsparseHybPartition_t28HIPSPARSE_HYB_PARTITION_AUTOE) Automatically decide on ELL nnz per row


-
enumerator HIPSPARSE_HYB_PARTITION_USER
[#](#_CPPv4N23hipsparseHybPartition_t28HIPSPARSE_HYB_PARTITION_USERE) User given ELL nnz per row


-
enumerator HIPSPARSE_HYB_PARTITION_MAX
[#](#_CPPv4N23hipsparseHybPartition_t27HIPSPARSE_HYB_PARTITION_MAXE) Max ELL nnz per row, no COO part


-
enumerator HIPSPARSE_HYB_PARTITION_AUTO

## hipsparseSolvePolicy_t[#](#hipsparsesolvepolicy-t)

-
enum hipsparseSolvePolicy_t
[#](#_CPPv422hipsparseSolvePolicy_t) Specify policy in triangular solvers and factorizations.

The

[hipsparseSolvePolicy_t](#hipsparse-types_8h_1a0d98e490c94d4facc231db60baf1c3b3)type indicates the solve policy for the triangular solve.*Values:*-
enumerator HIPSPARSE_SOLVE_POLICY_NO_LEVEL
[#](#_CPPv4N22hipsparseSolvePolicy_t31HIPSPARSE_SOLVE_POLICY_NO_LEVELE) No level information generated


-
enumerator HIPSPARSE_SOLVE_POLICY_USE_LEVEL
[#](#_CPPv4N22hipsparseSolvePolicy_t32HIPSPARSE_SOLVE_POLICY_USE_LEVELE) Generate level information


-
enumerator HIPSPARSE_SOLVE_POLICY_NO_LEVEL

## hipsparseDirection_t[#](#hipsparsedirection-t)

-
enum hipsparseDirection_t
[#](#_CPPv420hipsparseDirection_t) Specify the matrix direction.

The

[hipsparseDirection_t](#hipsparse-types_8h_1a8f704b6fc5ce97a1069c4a2c48d65b59)indicates whether a dense matrix should be parsed by rows or by columns, assuming column-major storage.*Values:*-
enumerator HIPSPARSE_DIRECTION_ROW
[#](#_CPPv4N20hipsparseDirection_t23HIPSPARSE_DIRECTION_ROWE) Parse the matrix by rows


-
enumerator HIPSPARSE_DIRECTION_COLUMN
[#](#_CPPv4N20hipsparseDirection_t26HIPSPARSE_DIRECTION_COLUMNE) Parse the matrix by columns


-
enumerator HIPSPARSE_DIRECTION_ROW

## hipsparseFormat_t[#](#hipsparseformat-t)

-
enum hipsparseFormat_t
[#](#_CPPv417hipsparseFormat_t) List of hipsparse sparse matrix formats.

This is a list of the

[hipsparseFormat_t](#hipsparse-generic-types_8h_1a775c0e17b2f7c40076f21942e05ecb97)types that are used by the hipSPARSE library.*Values:*-
enumerator HIPSPARSE_FORMAT_CSR
[#](#_CPPv4N17hipsparseFormat_t20HIPSPARSE_FORMAT_CSRE) Compressed Sparse Row


-
enumerator HIPSPARSE_FORMAT_CSC
[#](#_CPPv4N17hipsparseFormat_t20HIPSPARSE_FORMAT_CSCE) Compressed Sparse Column


-
enumerator HIPSPARSE_FORMAT_COO
[#](#_CPPv4N17hipsparseFormat_t20HIPSPARSE_FORMAT_COOE) Coordinate - Structure of Arrays


-
enumerator HIPSPARSE_FORMAT_COO_AOS
[#](#_CPPv4N17hipsparseFormat_t24HIPSPARSE_FORMAT_COO_AOSE) Coordinate - Array of Structures


-
enumerator HIPSPARSE_FORMAT_BLOCKED_ELL
[#](#_CPPv4N17hipsparseFormat_t28HIPSPARSE_FORMAT_BLOCKED_ELLE) Blocked ELL


-
enumerator HIPSPARSE_FORMAT_CSR

## hipsparseOrder_t[#](#hipsparseorder-t)

-
enum hipsparseOrder_t
[#](#_CPPv416hipsparseOrder_t) List of hipsparse dense matrix memory layout ordering.

This is a list of the

[hipsparseOrder_t](#hipsparse-generic-types_8h_1a3b39670348361eaf896d1c550cb8cddb)types that are used by the hipSPARSE library.*Values:*-
enumerator HIPSPARSE_DEPRECATED_MSG
[#](#_CPPv4N16hipsparseOrder_t24HIPSPARSE_DEPRECATED_MSGE) Column major


-
enumerator HIPSPARSE_ORDER_COL
[#](#_CPPv4N16hipsparseOrder_t19HIPSPARSE_ORDER_COLE) Column major


-
enumerator HIPSPARSE_ORDER_ROW
[#](#_CPPv4N16hipsparseOrder_t19HIPSPARSE_ORDER_ROWE) Row major


-
enumerator HIPSPARSE_DEPRECATED_MSG

## hipsparseIndextype_t[#](#hipsparseindextype-t)

-
enum hipsparseIndexType_t
[#](#_CPPv420hipsparseIndexType_t) List of hipsparse index type used by sparse matrix indices.

This is a list of the

[hipsparseIndexType_t](#hipsparse-generic-types_8h_1aaeacc98278238b4555b312b38a8ca3a1)types that are used by the hipSPARSE library.*Values:*-
enumerator HIPSPARSE_INDEX_16U
[#](#_CPPv4N20hipsparseIndexType_t19HIPSPARSE_INDEX_16UE) 16 bit unsigned integer indices


-
enumerator HIPSPARSE_INDEX_32I
[#](#_CPPv4N20hipsparseIndexType_t19HIPSPARSE_INDEX_32IE) 32 bit signed integer indices


-
enumerator HIPSPARSE_INDEX_64I
[#](#_CPPv4N20hipsparseIndexType_t19HIPSPARSE_INDEX_64IE) 64 bit signed integer indices


-
enumerator HIPSPARSE_INDEX_16U

## hipsparseCsr2CscAlg_t[#](#hipsparsecsr2cscalg-t)

-
enum hipsparseCsr2CscAlg_t
[#](#_CPPv421hipsparseCsr2CscAlg_t) List of hipsparse csr2csc algorithms.

This is a list of the

[hipsparseCsr2CscAlg_t](#hipsparse-types_8h_1aefbe2e155c187b47621bbf959e9dcebf)algorithms that can be used by the hipSPARSE library routines[hipsparseCsr2cscEx2_bufferSize](conversion.html#hipsparse__csr2csc_8h_1a9508f6d010bacdb65cb0b3b29f9e75cf)and[hipsparseCsr2cscEx2](conversion.html#hipsparse__csr2csc_8h_1a091d6b107db830512171e38ea51a54e6).*Values:*-
enumerator HIPSPARSE_CSR2CSC_ALG_DEFAULT
[#](#_CPPv4N21hipsparseCsr2CscAlg_t29HIPSPARSE_CSR2CSC_ALG_DEFAULTE)

-
enumerator HIPSPARSE_CSR2CSC_ALG1
[#](#_CPPv4N21hipsparseCsr2CscAlg_t22HIPSPARSE_CSR2CSC_ALG1E)

-
enumerator HIPSPARSE_CSR2CSC_ALG2
[#](#_CPPv4N21hipsparseCsr2CscAlg_t22HIPSPARSE_CSR2CSC_ALG2E)

-
enumerator HIPSPARSE_CSR2CSC_ALG_DEFAULT

## hipsparseSpMVAlg_t[#](#hipsparsespmvalg-t)

-
enum hipsparseSpMVAlg_t
[#](#_CPPv418hipsparseSpMVAlg_t) List of hipsparse SpMV algorithms.

This is a list of the

[hipsparseSpMVAlg_t](#hipsparse-generic-types_8h_1a2068975b2f22d616048a5e95ef77cd90)types that are used by the hipSPARSE library.*Values:*-
enumerator HIPSPARSE_MV_ALG_DEFAULT
[#](#_CPPv4N18hipsparseSpMVAlg_t24HIPSPARSE_MV_ALG_DEFAULTE)

-
enumerator HIPSPARSE_COOMV_ALG
[#](#_CPPv4N18hipsparseSpMVAlg_t19HIPSPARSE_COOMV_ALGE)

-
enumerator HIPSPARSE_CSRMV_ALG1
[#](#_CPPv4N18hipsparseSpMVAlg_t20HIPSPARSE_CSRMV_ALG1E)

-
enumerator HIPSPARSE_CSRMV_ALG2
[#](#_CPPv4N18hipsparseSpMVAlg_t20HIPSPARSE_CSRMV_ALG2E)

-
enumerator HIPSPARSE_SPMV_ALG_DEFAULT
[#](#_CPPv4N18hipsparseSpMVAlg_t26HIPSPARSE_SPMV_ALG_DEFAULTE)

-
enumerator HIPSPARSE_SPMV_COO_ALG1
[#](#_CPPv4N18hipsparseSpMVAlg_t23HIPSPARSE_SPMV_COO_ALG1E)

-
enumerator HIPSPARSE_SPMV_CSR_ALG1
[#](#_CPPv4N18hipsparseSpMVAlg_t23HIPSPARSE_SPMV_CSR_ALG1E)

-
enumerator HIPSPARSE_SPMV_CSR_ALG2
[#](#_CPPv4N18hipsparseSpMVAlg_t23HIPSPARSE_SPMV_CSR_ALG2E)

-
enumerator HIPSPARSE_SPMV_COO_ALG2
[#](#_CPPv4N18hipsparseSpMVAlg_t23HIPSPARSE_SPMV_COO_ALG2E)

-
enumerator HIPSPARSE_MV_ALG_DEFAULT

## hipsparseSpMMAlg_t[#](#hipsparsespmmalg-t)

-
enum hipsparseSpMMAlg_t
[#](#_CPPv418hipsparseSpMMAlg_t) List of hipsparse SpMM algorithms.

This is a list of the

[hipsparseSpMMAlg_t](#hipsparse-generic-types_8h_1ad5583e919ccd433146385003d863ee40)types that are used by the hipSPARSE library.*Values:*-
enumerator HIPSPARSE_MM_ALG_DEFAULT
[#](#_CPPv4N18hipsparseSpMMAlg_t24HIPSPARSE_MM_ALG_DEFAULTE) Default algorithm


-
enumerator HIPSPARSE_COOMM_ALG1
[#](#_CPPv4N18hipsparseSpMMAlg_t20HIPSPARSE_COOMM_ALG1E) COO algorithm 1


-
enumerator HIPSPARSE_COOMM_ALG2
[#](#_CPPv4N18hipsparseSpMMAlg_t20HIPSPARSE_COOMM_ALG2E) COO algorithm 2


-
enumerator HIPSPARSE_COOMM_ALG3
[#](#_CPPv4N18hipsparseSpMMAlg_t20HIPSPARSE_COOMM_ALG3E) COO algorithm 3


-
enumerator HIPSPARSE_CSRMM_ALG1
[#](#_CPPv4N18hipsparseSpMMAlg_t20HIPSPARSE_CSRMM_ALG1E) CSR algorithm 1


-
enumerator HIPSPARSE_SPMM_ALG_DEFAULT
[#](#_CPPv4N18hipsparseSpMMAlg_t26HIPSPARSE_SPMM_ALG_DEFAULTE) Default algorithm


-
enumerator HIPSPARSE_SPMM_COO_ALG1
[#](#_CPPv4N18hipsparseSpMMAlg_t23HIPSPARSE_SPMM_COO_ALG1E) COO algorithm 1


-
enumerator HIPSPARSE_SPMM_COO_ALG2
[#](#_CPPv4N18hipsparseSpMMAlg_t23HIPSPARSE_SPMM_COO_ALG2E) COO algorithm 2


-
enumerator HIPSPARSE_SPMM_COO_ALG3
[#](#_CPPv4N18hipsparseSpMMAlg_t23HIPSPARSE_SPMM_COO_ALG3E) COO algorithm 3


-
enumerator HIPSPARSE_SPMM_COO_ALG4
[#](#_CPPv4N18hipsparseSpMMAlg_t23HIPSPARSE_SPMM_COO_ALG4E) COO algorithm 4


-
enumerator HIPSPARSE_SPMM_CSR_ALG1
[#](#_CPPv4N18hipsparseSpMMAlg_t23HIPSPARSE_SPMM_CSR_ALG1E) CSR algorithm 1


-
enumerator HIPSPARSE_SPMM_CSR_ALG2
[#](#_CPPv4N18hipsparseSpMMAlg_t23HIPSPARSE_SPMM_CSR_ALG2E) CSR algorithm 2


-
enumerator HIPSPARSE_SPMM_CSR_ALG3
[#](#_CPPv4N18hipsparseSpMMAlg_t23HIPSPARSE_SPMM_CSR_ALG3E) CSR algorithm 3


-
enumerator HIPSPARSE_SPMM_BLOCKED_ELL_ALG1
[#](#_CPPv4N18hipsparseSpMMAlg_t31HIPSPARSE_SPMM_BLOCKED_ELL_ALG1E) Blocked ELL algorithm 1


-
enumerator HIPSPARSE_MM_ALG_DEFAULT

## hipsparseSparseToDenseAlg_t[#](#hipsparsesparsetodensealg-t)

-
enum hipsparseSparseToDenseAlg_t
[#](#_CPPv427hipsparseSparseToDenseAlg_t) List of hipsparse SparseToDense algorithms.

This is a list of the

[hipsparseSparseToDenseAlg_t](#hipsparse-generic-types_8h_1a8cf693cd63257327a118972804efa6b0)types that are used by the hipSPARSE library.*Values:*-
enumerator HIPSPARSE_SPARSETODENSE_ALG_DEFAULT
[#](#_CPPv4N27hipsparseSparseToDenseAlg_t35HIPSPARSE_SPARSETODENSE_ALG_DEFAULTE)

-
enumerator HIPSPARSE_SPARSETODENSE_ALG_DEFAULT

## hipsparseDenseToSparseAlg_t[#](#hipsparsedensetosparsealg-t)

-
enum hipsparseDenseToSparseAlg_t
[#](#_CPPv427hipsparseDenseToSparseAlg_t) List of hipsparse DenseToSparse algorithms.

This is a list of the

[hipsparseDenseToSparseAlg_t](#hipsparse-generic-types_8h_1a10ebd1409efe5d4093cf02c8b4ef0a12)types that are used by the hipSPARSE library.*Values:*-
enumerator HIPSPARSE_DENSETOSPARSE_ALG_DEFAULT
[#](#_CPPv4N27hipsparseDenseToSparseAlg_t35HIPSPARSE_DENSETOSPARSE_ALG_DEFAULTE)

-
enumerator HIPSPARSE_DENSETOSPARSE_ALG_DEFAULT

## hipsparseSDDMMAlg_t[#](#hipsparsesddmmalg-t)

-
enum hipsparseSDDMMAlg_t
[#](#_CPPv419hipsparseSDDMMAlg_t) List of hipsparse SDDMM algorithms.

This is a list of the

[hipsparseSDDMMAlg_t](#hipsparse-generic-types_8h_1a0b36175e84d5df7b4ce4ded56ccf1195)types that are used by the hipSPARSE library.*Values:*-
enumerator HIPSPARSE_SDDMM_ALG_DEFAULT
[#](#_CPPv4N19hipsparseSDDMMAlg_t27HIPSPARSE_SDDMM_ALG_DEFAULTE)

-
enumerator HIPSPARSE_SDDMM_ALG_DEFAULT

## hipsparseSpSVAlg_t[#](#hipsparsespsvalg-t)

-
enum hipsparseSpSVAlg_t
[#](#_CPPv418hipsparseSpSVAlg_t) List of hipsparse SpSV algorithms.

This is a list of the

[hipsparseSpSVAlg_t](#hipsparse-generic-types_8h_1a8dc2f204c937a49240baf239f82cddc0)types that are used by the hipSPARSE library.*Values:*-
enumerator HIPSPARSE_SPSV_ALG_DEFAULT
[#](#_CPPv4N18hipsparseSpSVAlg_t26HIPSPARSE_SPSV_ALG_DEFAULTE)

-
enumerator HIPSPARSE_SPSV_ALG_DEFAULT

## hipsparseSpSMAlg_t[#](#hipsparsespsmalg-t)

-
enum hipsparseSpSMAlg_t
[#](#_CPPv418hipsparseSpSMAlg_t) List of hipsparse SpSM algorithms.

This is a list of the

[hipsparseSpSMAlg_t](#hipsparse-generic-types_8h_1a7b1cc3961fe25f0914e40e9234f8159e)types that are used by the hipSPARSE library.*Values:*-
enumerator HIPSPARSE_SPSM_ALG_DEFAULT
[#](#_CPPv4N18hipsparseSpSMAlg_t26HIPSPARSE_SPSM_ALG_DEFAULTE)

-
enumerator HIPSPARSE_SPSM_ALG_DEFAULT

## hipsparseSpMatAttribute_t[#](#hipsparsespmatattribute-t)

-
enum hipsparseSpMatAttribute_t
[#](#_CPPv425hipsparseSpMatAttribute_t) List of hipsparse attributes.

This is a list of the

[hipsparseSpMatAttribute_t](#hipsparse-generic-types_8h_1af4847d65bd974e3e088bf72127191fa8)types that are used by the hipSPARSE library.*Values:*-
enumerator HIPSPARSE_SPMAT_FILL_MODE
[#](#_CPPv4N25hipsparseSpMatAttribute_t25HIPSPARSE_SPMAT_FILL_MODEE) Fill mode attribute


-
enumerator HIPSPARSE_SPMAT_DIAG_TYPE
[#](#_CPPv4N25hipsparseSpMatAttribute_t25HIPSPARSE_SPMAT_DIAG_TYPEE) Diag type attribute


-
enumerator HIPSPARSE_SPMAT_FILL_MODE

## hipsparseSpGEMMAlg_t[#](#hipsparsespgemmalg-t)

-
enum hipsparseSpGEMMAlg_t
[#](#_CPPv420hipsparseSpGEMMAlg_t) List of hipsparse SpGEMM algorithms.

This is a list of the

[hipsparseSpGEMMAlg_t](#hipsparse-generic-types_8h_1acc1dd7c301c1e1a3e1bffe3b65074d4d)types that are used by the hipSPARSE library.*Values:*-
enumerator HIPSPARSE_SPGEMM_DEFAULT
[#](#_CPPv4N20hipsparseSpGEMMAlg_t24HIPSPARSE_SPGEMM_DEFAULTE)

-
enumerator HIPSPARSE_SPGEMM_CSR_ALG_DETERMINISTIC
[#](#_CPPv4N20hipsparseSpGEMMAlg_t38HIPSPARSE_SPGEMM_CSR_ALG_DETERMINISTICE)

-
enumerator HIPSPARSE_SPGEMM_CSR_ALG_NONDETERMINISTIC
[#](#_CPPv4N20hipsparseSpGEMMAlg_t41HIPSPARSE_SPGEMM_CSR_ALG_NONDETERMINISTICE)

-
enumerator HIPSPARSE_SPGEMM_ALG1
[#](#_CPPv4N20hipsparseSpGEMMAlg_t21HIPSPARSE_SPGEMM_ALG1E)

-
enumerator HIPSPARSE_SPGEMM_ALG2
[#](#_CPPv4N20hipsparseSpGEMMAlg_t21HIPSPARSE_SPGEMM_ALG2E)

-
enumerator HIPSPARSE_SPGEMM_ALG3
[#](#_CPPv4N20hipsparseSpGEMMAlg_t21HIPSPARSE_SPGEMM_ALG3E)

-
enumerator HIPSPARSE_SPGEMM_DEFAULT
