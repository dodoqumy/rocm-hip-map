import React from 'react';
import {beforeEach, describe, expect, it, vi} from 'vitest';
import {fireEvent, render, screen, waitFor} from '@testing-library/react';
import PriceTracker from './PriceTracker';

const fetchMock = vi.fn();

describe('PriceTracker', () => {
  beforeEach(() => {
    fetchMock.mockReset();
    vi.stubGlobal('fetch', fetchMock);
  });

  it('renders fetched price entries and filters by category', async () => {
    fetchMock.mockResolvedValue({
      ok: true,
      json: async () => ({
        updated: '2026-05-02T00:00:00Z',
        week: '2026-W18',
        rates: {USD: 1},
        entries: [
          {
            gpu_id: 'AMD_Instinct_MI210',
            gpu_name: 'AMD Instinct MI210',
            country: 'US',
            platform: 'eBay',
            condition: 'used',
            currency_original: 'USD',
            median_usd: 3200,
            min_usd: 3000,
            max_usd: 3400,
            sample_size: 3,
            original_sample_size: 3,
            source_url: 'https://example.com/mi210',
            collected_at: '2026-05-02T00:00:00Z',
          },
          {
            gpu_id: 'AMD_Radeon_RX_7900_XTX',
            gpu_name: 'AMD Radeon RX 7900 XTX',
            country: 'DE',
            platform: 'eBay',
            condition: 'used',
            currency_original: 'EUR',
            median_usd: 850,
            min_usd: 800,
            max_usd: 900,
            sample_size: 5,
            original_sample_size: 5,
            source_url: 'https://example.com/7900xtx',
            collected_at: '2026-05-02T00:00:00Z',
          },
        ],
      }),
    });

    render(<PriceTracker />);

    await waitFor(() => {
      expect(screen.getByText('AMD Instinct MI210')).toBeInTheDocument();
    });

    fireEvent.click(screen.getByRole('button', {name: '🧮 Instinct 计算卡'}));

    expect(screen.getByText('AMD Instinct MI210')).toBeInTheDocument();
    expect(screen.queryByText('AMD Radeon RX 7900 XTX')).not.toBeInTheDocument();
  });

  it('shows the empty-data message when both fetch attempts fail', async () => {
    fetchMock.mockRejectedValue(new Error('network'));

    render(<PriceTracker />);

    await waitFor(() => {
      expect(screen.getByText('📊 暂无价格数据。等待首次数据采集后自动显示。')).toBeInTheDocument();
    });
  });
});
