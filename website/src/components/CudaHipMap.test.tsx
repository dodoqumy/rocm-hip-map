import React from 'react';
import {beforeEach, describe, expect, it, vi} from 'vitest';
import {fireEvent, render, screen, waitFor} from '@testing-library/react';
import CudaHipMap from './CudaHipMap';

const fetchMock = vi.fn();

describe('CudaHipMap', () => {
  beforeEach(() => {
    fetchMock.mockReset();
    vi.stubGlobal('fetch', fetchMock);
  });

  it('loads fetched mappings and filters by search term', async () => {
    fetchMock.mockResolvedValue({
      ok: true,
      json: async () => [
        {cuda: 'cudaMalloc', hip: 'hipMalloc', category: '内存管理', status: 'supported', notes: ''},
        {cuda: 'cudaGraphLaunch', hip: 'hipGraphLaunch', category: '执行控制', status: 'supported', notes: 'graph'},
      ],
    });

    render(<CudaHipMap />);

    await waitFor(() => {
      expect(screen.getByText('cudaGraphLaunch')).toBeInTheDocument();
    });

    fireEvent.change(screen.getByPlaceholderText('搜索 CUDA 或 HIP API...'), {
      target: {value: 'graph'},
    });

    expect(screen.getByText('cudaGraphLaunch')).toBeInTheDocument();
    expect(screen.queryByText('cudaMalloc')).not.toBeInTheDocument();
  });
});
