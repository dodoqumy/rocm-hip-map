import type { SidebarsConfig } from '@docusaurus/plugin-content-docs';

// 由 scripts/generate-sidebar.py 自动生成
// 手动编辑后运行 python3 scripts/generate-sidebar.py 覆盖

const sidebars: SidebarsConfig = {
  docs: [
    {
      type: 'category',
      label: '🚀 入门指南',
      collapsible: true,
      collapsed: false,
      link: { type: 'doc', id: 'getting-started/index' },
      items: ['getting-started/what-is-rocm'],
    },
    {
      type: 'category',
      label: '💻 HIP 编程',
      collapsible: true,
      collapsed: false,
      items: [
        {
          type: 'category',
          label: '参考',
          collapsible: true,
          collapsed: true,
          items: [
            'hip/参考/hip_projects_HIP_en_latest_reference_index',
          ],
        },
        {
          type: 'category',
          label: '总览',
          collapsible: true,
          collapsed: true,
          items: [
            'hip/总览/hip_projects_HIP_en_latest_index',
          ],
        },
        {
          type: 'category',
          label: '操作指南',
          collapsible: true,
          collapsed: true,
          items: [
            'hip/操作指南/hip_projects_HIP_en_latest_how-to_hip_debugging',
            'hip/操作指南/hip_projects_HIP_en_latest_how-to_hip_install',
            'hip/操作指南/hip_projects_HIP_en_latest_how-to_hip_porting_guide',
          ],
        },
      ],
    },
    {
      type: 'category',
      label: '🔄 HIPIFY 迁移',
      collapsible: true,
      collapsed: false,
      items: [
        {
          type: 'category',
          label: '总览',
          collapsible: true,
          collapsed: true,
          items: [
            'hipify/总览/hipify_projects_HIPIFY_en_latest_hipify-clang',
            'hipify/总览/hipify_projects_HIPIFY_en_latest_hipify-perl',
            'hipify/总览/hipify_projects_HIPIFY_en_latest_index',
            'hipify/总览/hipify_projects_HIPIFY_en_latest_supported_apis',
          ],
        },
      ],
    },
    {
      type: 'category',
      label: '📥 安装指南',
      collapsible: true,
      collapsed: false,
      items: [
        {
          type: 'category',
          label: '参考',
          collapsible: true,
          collapsed: true,
          items: [
            'install/参考/rocm-install-linux_projects_install-on-linux_en_latest_reference_system-requirements',
          ],
        },
        {
          type: 'category',
          label: '安装步骤',
          collapsible: true,
          collapsed: true,
          items: [
            'install/安装步骤/rocm-install-linux_projects_install-on-linux_en_latest_install_install-amdgpu',
            'install/安装步骤/rocm-install-linux_projects_install-on-linux_en_latest_install_install-post',
            'install/安装步骤/rocm-install-linux_projects_install-on-linux_en_latest_install_install-quick',
          ],
        },
        {
          type: 'category',
          label: '总览',
          collapsible: true,
          collapsed: true,
          items: [
            'install/总览/rocm-install-linux_projects_install-on-linux_en_latest_index',
          ],
        },
      ],
    },
    {
      type: 'category',
      label: '📦 ROCm 核心文档',
      collapsible: true,
      collapsed: false,
      items: [
        {
          type: 'category',
          label: 'About',
          collapsible: true,
          collapsed: true,
          items: [
            'rocm-core/about/rocm_en_latest_about_license',
          ],
        },
        {
          type: 'category',
          label: 'GPU 性能',
          collapsible: true,
          collapsed: true,
          items: [
            'rocm-core/gpu-性能/rocm_en_latest_how-to_gpu-performance_mi300x',
          ],
        },
        {
          type: 'category',
          label: 'ROCm for AI',
          collapsible: true,
          collapsed: true,
          items: [
            'rocm-core/rocm-for-ai/rocm_en_latest_how-to_rocm-for-ai_fine-tuning_index',
            'rocm-core/rocm-for-ai/rocm_en_latest_how-to_rocm-for-ai_index',
            'rocm-core/rocm-for-ai/rocm_en_latest_how-to_rocm-for-ai_inference-optimization_index',
            'rocm-core/rocm-for-ai/rocm_en_latest_how-to_rocm-for-ai_inference-optimization_model-quantization',
            'rocm-core/rocm-for-ai/rocm_en_latest_how-to_rocm-for-ai_inference_deploy-your-model',
            'rocm-core/rocm-for-ai/rocm_en_latest_how-to_rocm-for-ai_inference_hugging-face-models',
            'rocm-core/rocm-for-ai/rocm_en_latest_how-to_rocm-for-ai_inference_index',
            'rocm-core/rocm-for-ai/rocm_en_latest_how-to_rocm-for-ai_inference_llm-inference-frameworks',
            'rocm-core/rocm-for-ai/rocm_en_latest_how-to_rocm-for-ai_install',
            'rocm-core/rocm-for-ai/rocm_en_latest_how-to_rocm-for-ai_system-setup_index',
            'rocm-core/rocm-for-ai/rocm_en_latest_how-to_rocm-for-ai_training_index',
            'rocm-core/rocm-for-ai/rocm_en_latest_how-to_rocm-for-ai_training_scale-model-training',
          ],
        },
        {
          type: 'category',
          label: 'ROCm for HPC',
          collapsible: true,
          collapsed: true,
          items: [
            'rocm-core/rocm-for-hpc/rocm_en_latest_how-to_rocm-for-hpc_index',
          ],
        },
        {
          type: 'category',
          label: '兼容性',
          collapsible: true,
          collapsed: true,
          items: [
            'rocm-core/兼容性/rocm_en_latest_compatibility_ml-compatibility_dgl',
            'rocm-core/兼容性/rocm_en_latest_compatibility_ml-compatibility_jax',
            'rocm-core/兼容性/rocm_en_latest_compatibility_ml-compatibility_pytorch',
            'rocm-core/兼容性/rocm_en_latest_compatibility_ml-compatibility_tensorflow',
          ],
        },
        {
          type: 'category',
          label: '参考',
          collapsible: true,
          collapsed: true,
          items: [
            'rocm-core/参考/rocm_en_latest_reference_api-libraries',
            'rocm-core/参考/rocm_en_latest_reference_env-variables',
            'rocm-core/参考/rocm_en_latest_reference_gpu-arch-specs',
            'rocm-core/参考/rocm_en_latest_reference_graph-safe-support',
            'rocm-core/参考/rocm_en_latest_reference_precision-support',
            'rocm-core/参考/rocm_en_latest_reference_rocm-tools',
          ],
        },
        {
          type: 'category',
          label: '性能调优',
          collapsible: true,
          collapsed: true,
          items: [
            'rocm-core/性能调优/rocm_en_latest_how-to_tuning-guides_mi300x_index',
          ],
        },
        {
          type: 'category',
          label: '总览',
          collapsible: true,
          collapsed: true,
          items: [
            'rocm-core/总览/rocm_en_latest_index',
            'rocm-core/总览/rocm_en_latest_what-is-rocm',
          ],
        },
        {
          type: 'category',
          label: '操作指南',
          collapsible: true,
          collapsed: true,
          items: [
            'rocm-core/操作指南/rocm_en_latest_how-to_Bar-Memory',
            'rocm-core/操作指南/rocm_en_latest_how-to_build-rocm',
            'rocm-core/操作指南/rocm_en_latest_how-to_deep-learning-rocm',
            'rocm-core/操作指南/rocm_en_latest_how-to_programming_guide',
            'rocm-core/操作指南/rocm_en_latest_how-to_setting-cus',
            'rocm-core/操作指南/rocm_en_latest_how-to_system-debugging',
          ],
        },
        {
          type: 'category',
          label: '术语表',
          collapsible: true,
          collapsed: true,
          items: [
            'rocm-core/术语表/rocm_en_latest_reference_glossary_index',
          ],
        },
        {
          type: 'category',
          label: '概念',
          collapsible: true,
          collapsed: true,
          items: [
            'rocm-core/概念/rocm_en_latest_conceptual_ai-pytorch-inception',
            'rocm-core/概念/rocm_en_latest_conceptual_cmake-packages',
            'rocm-core/概念/rocm_en_latest_conceptual_compiler-topics',
            'rocm-core/概念/rocm_en_latest_conceptual_file-reorg',
            'rocm-core/概念/rocm_en_latest_conceptual_gpu-arch',
            'rocm-core/概念/rocm_en_latest_conceptual_gpu-arch_mi100',
            'rocm-core/概念/rocm_en_latest_conceptual_gpu-arch_mi250',
            'rocm-core/概念/rocm_en_latest_conceptual_gpu-arch_mi300',
            'rocm-core/概念/rocm_en_latest_conceptual_gpu-isolation',
          ],
        },
        {
          type: 'category',
          label: '系统优化',
          collapsible: true,
          collapsed: true,
          items: [
            'rocm-core/系统优化/rocm_en_latest_how-to_system-optimization_index',
            'rocm-core/系统优化/rocm_en_latest_how-to_system-optimization_rdna3_5',
          ],
        },
        {
          type: 'category',
          label: '贡献',
          collapsible: true,
          collapsed: true,
          items: [
            'rocm-core/贡献/rocm_en_latest_contribute_building',
            'rocm-core/贡献/rocm_en_latest_contribute_contributing',
            'rocm-core/贡献/rocm_en_latest_contribute_toolchain',
          ],
        },
      ],
    },
    {
      type: 'category',
      label: '📜 论文检索',
      collapsible: true,
      collapsed: true,
      link: { type: 'doc', id: 'papers/index' },
      items: [],  // auto-generated, too many to list
    },
    {
      type: 'category',
      label: '🌐 多语言情报',
      collapsible: true,
      collapsed: true,
      link: { type: 'doc', id: 'multilingual/index' },
      items: [
        {
          type: "category",
          label: "🇬🇧 英语 (14)",
          collapsible: true,
          collapsed: true,
          items: [
            "multilingual/en/bsc_bsc",
            "multilingual/en/csc-en_csc-webinars",
            "multilingual/en/csc-lumi_csc-lumi-training",
            "multilingual/en/csc-lumi_csc-lumi",
            "multilingual/en/genci_genci-en",
            "multilingual/en/julich_forschungszentrum-j-lich-jsc",
            "multilingual/en/lrz_lrz",
            "multilingual/en/nsc-sv_nsc-support",
            "multilingual/en/nsc-sv_nsc",
            "multilingual/en/pdc-kth_pdc-kth",
            "multilingual/en/riken_riken-en",
            "multilingual/en/surf_surf-hpc-wiki",
            "multilingual/en/surf_surf-hpc",
            "multilingual/en/uppmax_uppmax",
          ],
        },
        {
          type: "category",
          label: "🇯🇵 日语 (8)",
          collapsible: true,
          collapsed: true,
          items: [
            "multilingual/ja/cinii_cinii",
            "multilingual/ja/osaka-u-cybermedia_article-5058",
            "multilingual/ja/osaka-u-cybermedia_article-8138",
            "multilingual/ja/titech-tsubame_tsubame-4-0-docs",
            "multilingual/ja/titech-tsubame_tsubame-4-0-en",
            "multilingual/ja/u-tokyo-hpc_article-1774",
            "multilingual/ja/u-tokyo-hpc_article-6777",
            "multilingual/ja/u-tokyo-hpc_guide",
          ],
        },
        {
          type: "category",
          label: "🇰🇷 韩语 (3)",
          collapsible: true,
          collapsed: true,
          items: [
            "multilingual/ko/kaist_kaist",
            "multilingual/ko/kisti_kisti",
            "multilingual/ko/snu-hpc_hpc",
          ],
        },
        {
          type: "category",
          label: "🇷🇺 俄语 (2)",
          collapsible: true,
          collapsed: true,
          items: [
            "multilingual/ru/msu-hpc_article-25",
            "multilingual/ru/msu-hpc_article-2585",
          ],
        },
      ],
    },
    {
      type: 'category',
      label: '📋 兼容性矩阵',
      collapsible: true,
      collapsed: true,
      link: { type: 'doc', id: 'compatibility/overview' },
      items: [],
    },
    {
      type: 'category',
      label: '🔄 CUDA → HIP',
      collapsible: true,
      collapsed: true,
      link: { type: 'doc', id: 'cuda-to-hip/api-map' },
      items: [],
    },
    {
      type: 'category',
      label: '❗ 错误码库',
      collapsible: true,
      collapsed: true,
      link: { type: 'doc', id: 'errors/index' },
      items: [],
    },
    {
      type: 'category',
      label: '📡 Issue 情报',
      collapsible: true,
      collapsed: true,
      link: { type: 'doc', id: 'issues/index' },
      items: [],
    },
    {
      type: "category",
      label: "📜 技术论文",
      collapsible: true,
      collapsed: true,
      items: [
        {
          type: "category",
          label: "⚡ 分布式与系统 (34)",
          collapsible: true,
          collapsed: true,
          items: [
            "papers/2406.10362v1",  // A Comparison of the Performance of the Molecular Dynamics Si
            "papers/2309.04671v2",  // A Portable Framework for Accelerating Stencil Computations o
            "papers/2411.05009v1",  // A Study of Performance Portability in Plasma Physics Simulat
            "papers/2604.18616v1",  // ARGUS: Agentic GPU Optimization Guided by Data-Flow Invarian
            "papers/2603.16428v1",  // An Efficient Heterogeneous Co-Design for Fine-Tuning on a Si
            "papers/2412.08308v3",  // Analyzing the Performance Portability of SYCL across CPUs, G
            "papers/2304.06835v3",  // Automated Translation and Accelerated Solving of Differentia
            "papers/2407.11488v1",  // Bringing Auto-tuning to HIP: Analysis of Tuning Impact and D
            "papers/2502.16631v1",  // CRIUgpu: Transparent Checkpointing of GPU-Accelerated Worklo
            "papers/2512.08242v1",  // Chopper: A Multi-Level GPU Characterization Tool & Derived I
            "papers/2511.06605v2",  // DMA-Latte: Expanding the Reach of DMA Offloads to Latency-bo
            "papers/2303.06195v1",  // Evaluating performance and portability of high-level program
            "papers/2604.06056v2",  // Fine-Grained Power and Energy Attribution on AMD GPU/APU-Bas
            "papers/2512.22147v1",  // GPU Kernel Optimization Beyond Full Builds: An LLM Framework
            "papers/2207.04584v1",  // HEGrid: A High Efficient Multi-Channel Radio Astronomical Da
            "papers/2601.22585v1",  // HetCCL: Accelerating LLM Training with Heterogeneous GPUs
            "papers/2508.11298v2",  // Inter-APU Communication on AMD MI300A Systems via Infinity F
            "papers/2309.10292v3",  // Julia as a unifying end-to-end workflow language on the Fron
            "papers/2511.09861v2",  // Lit Silicon: A Case Where Thermal Imbalance Couples Concurre
            "papers/2604.07276v1",  // Making Room for AI: Multi-GPU Molecular Dynamics with Deep P
            "papers/2508.10202v2",  // Mixed-Precision Performance Portability of FFT-Based GPU-Acc
            "papers/2509.21039v1",  // Mojo: MLIR-Based Performance-Portable HPC Science Kernels on
            "papers/2310.06947v1",  // Open SYCL on heterogeneous GPU systems: A case of study
            "papers/2403.06931v1",  // Optimizing sDTW for AMD GPUs
            "papers/2405.00436v1",  // Porting HPC Applications to AMD Instinct$^text{TM}$ MI300A U
            "papers/2401.02680v1",  // Preliminary report: Initial evaluation of StdPar implementat
            "papers/2601.11822v1",  // RAPID-Serve: Resource-efficient and Accelerated P/D Intra-GP
            "papers/2303.08058v2",  // Stellar Mergers with HPX-Kokkos and SYCL: Methods of using a
            "papers/2408.11417v2",  // Stream-K++: Adaptive GPU GEMM Kernel Scheduling and Selectio
            "papers/2402.08950v4",  // Taking GPU Programming Models to Task for Performance Portab
            "papers/2604.06056v2",  // Token-Budget-Aware Pool Routing for Cost-Efficient LLM Infer
            "papers/2603.28793v1",  // Toward a Universal GPU Instruction Set Architecture: A Cross
            "papers/2603.29002v1",  // Understand and Accelerate Memory Processing Pipeline for Dis
            "papers/2402.06384v1",  // pSTL-Bench: A Micro-Benchmark Suite for Assessing Scalabilit
          ],
        },
        {
          type: "category",
          label: "🔧 架构与硬件 (10)",
          collapsible: true,
          collapsed: true,
          items: [
            "papers/2603.05931v1",  // A Persistent-State Dataflow Accelerator for Memory-Bound Lin
            "papers/2603.10031v1",  // Architecture-Aware LLM Inference Optimization on AMD Instinc
            "papers/2505.16968v4",  // CASS: Nvidia to AMD Transpilation with Data, Models, and Ben
            "papers/2603.08747v1",  // Diagnosing FP4 inference: a layer-wise and block-wise sensit
            "papers/2412.12426v2",  // FinGraV: Methodology for Fine-Grain GPU Power Visibility and
            "papers/2604.15379v1",  // Fleet: Hierarchical Task-based Abstraction for Megakernels o
            "papers/2601.15710v1",  // FlexLLM: Composable HLS Library for Flexible Hybrid LLM Acce
            "papers/2309.11001v1",  // GME: GPU-based Microarchitectural Extensions to Accelerate H
            "papers/2603.14785v1",  // SkipOPU: An FPGA-based Overlay Processor for Large Language 
            "papers/2604.10852v1",  // The xPU-athalon: Quantifying the Competition of AI Accelerat
          ],
        },
        {
          type: "category",
          label: "🤖 AI/ML (10)",
          collapsible: true,
          collapsed: true,
          items: [
            "papers/2603.12646v1",  // 98$times$ Faster LLM Routing Without a Dedicated GPU: Flash 
            "papers/1607.00592v1",  // Automatic Techniques for Gridding cDNA Microarray Images
            "papers/2604.02344v1",  // Characterizing WebGPU Dispatch Overhead for LLM Inference Ac
            "papers/2104.08178v1",  // Design of an Efficient, Ease-of-use and Affordable Artificia
            "papers/2604.08075v1",  // Dual-Pool Token-Budget Routing for Cost-Efficient and Reliab
            "papers/2511.10628v2",  // Instella: Fully Open Language Models with Stellar Performanc
            "papers/2604.24169v1",  // PointTransformerX:Portable and Efficient 3D Point Cloud Proc
            "papers/1802.02975v1",  // Practical Issues of Action-conditioned Next Image Prediction
            "papers/2505.02146v1",  // QiMeng-Xpiler: Transcompiling Tensor Programs for Deep Learn
            "papers/2505.07046v1",  // Streaming Krylov-Accelerated Stochastic Gradient Descent
          ],
        },
        {
          type: "category",
          label: "📊 性能优化 (3)",
          collapsible: true,
          collapsed: true,
          items: [
            "papers/2310.16122v1",  // A Performance-Portable SYCL Implementation of CRK-HACC for E
            "papers/2309.10075v1",  // Evaluating the performance portability of SYCL across CPUs a
            "papers/2508.04917v1",  // Mapping Sparse Triangular Solves to GPUs via Fine-grained Do
          ],
        },
        {
          type: "category",
          label: "📝 编程语言与编译器 (3)",
          collapsible: true,
          collapsed: true,
          items: [
            "papers/2107.07809v1",  // A method for decompilation of AMD GCN kernels to OpenCL
            "papers/2309.09609v2",  // Comparing Performance and Portability between CUDA and SYCL 
            "papers/2410.09172v1",  // Testing GPU Numerics: Finding Numerical Differences Between 
          ],
        },
        {
          type: "category",
          label: "🔬 建模与仿真 (1)",
          collapsible: true,
          collapsed: true,
          items: [
            "papers/2409.10729v1",  // OpenACC offloading of the MFC compressible multiphase flow s
          ],
        },
        {
          type: "category",
          label: "🧬 生物信息 (8)",
          collapsible: true,
          collapsed: true,
          items: [
            "papers/1806.03142v2",  // CLEAR: Coverage-based Limiting-cell Experiment Analysis for 
            "papers/2001.03092v1",  // De Novo Assembly of Uca minax Transcriptome from Next Genera
            "papers/1705.08246v1",  // IGoR: a tool for high-throughput immune repertoire analysis
            "papers/1708.01492v5",  // Minimap2: pairwise alignment for nucleotide sequences
            "papers/2310.12979v2",  // Predicting a Protein's Stability under a Million Mutations
            "papers/2410.10911v1",  // Quantum-Enhanced Detection of Viral cDNA via Luminescence Re
            "papers/2509.16328v2",  // The Role of High-Performance GPU Resources in Large Language
            "papers/2308.05118v1",  // Vector Embeddings by Sequence Similarity and Context for Imp
          ],
        },
        {
          type: "category",
          label: "📄 其他 (18)",
          collapsible: true,
          collapsed: true,
          items: [
            "papers/1610.02895v1",  // A Novel Collaborative Cognitive Dynamic Network Architecture
            "papers/2508.16806v1",  // Accelerating a Linear Programming Algorithm on AMD GPUs
            "papers/1702.01875v1",  // Adaptive Basis Selection for Exponential Family Smoothing Sp
            "papers/1809.08805v1",  // Data and Spectrum Trading Policies in a Trusted Cognitive Dy
            "papers/2601.17526v1",  // Evaluating Application Characteristics for GPU Portability L
            "papers/2302.00850v1",  // Evolving the COLA software library
            "papers/2507.20719v1",  // Exascale Implicit Kinetic Plasma Simulations on El~Capitan f
            "papers/2301.10838v2",  // Fast Merge Tree Computation via SYCL
            "papers/2512.04447v2",  // GPU-Portable Real-Space Density Functional Theory Implementa
            "papers/2512.21697v1",  // GaDE -- GPU-acceleration of time-dependent Dirac Equation fo
            "papers/2203.06777v1",  // Grid: OneCode and FourAPIs
            "papers/1706.09487v1",  // Parameterized Algorithms for Partitioning Graphs into Highly
            "papers/2502.03249v1",  // Portable Lattice QCD implementation based on OpenCL
            "papers/2406.02201v1",  // Porting the grid-based 3D+3V hybrid-Vlasov kinetic plasma si
            "papers/2408.16509v1",  // PyFR v2.0.3: Towards Industrial Adoption of Scale-Resolving 
            "papers/2603.00292v1",  // Ray Tracing using HIP
            "papers/2402.08161v2",  // The Monte Carlo Computational Summit -- October 25 & 26, 202
            "papers/2002.07050v1",  // Ultrasensitive THz Biosensor for PCR-free cDNA detection bas
          ],
        },
      ],
    },
    {
      type: 'category',
      label: '💰 GPU 二手价格',
      collapsible: true,
      collapsed: true,
      link: { type: 'doc', id: 'prices/index' },
      items: [],
    },
  ],
};

export default sidebars;
