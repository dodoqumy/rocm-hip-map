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
            'rocm-core/about/rocm_en_latest_about_release-notes',
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
            'rocm-core/兼容性/rocm_en_latest_compatibility_compatibility-matrix',
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
            'rocm-core/参考/rocm_en_latest_reference_gpu-atomics-operation',
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
          label: '版本发布',
          collapsible: true,
          collapsed: true,
          items: [
            'rocm-core/版本发布/rocm_en_latest_release_changelog',
            'rocm-core/版本发布/rocm_en_latest_release_versions',
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
      items: [],  // auto-generated
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
  ],
};

export default sidebars;
