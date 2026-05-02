import path from 'node:path';
import {defineConfig} from 'vitest/config';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@site': path.resolve(__dirname, '.'),
      '@theme': path.resolve(__dirname, 'src/theme'),
      '@theme-original': path.resolve(__dirname, 'node_modules/@docusaurus/theme-classic/src/theme'),
      '@theme-init': path.resolve(__dirname, 'node_modules/@docusaurus/theme-classic/src/theme'),
      '@generated': path.resolve(__dirname, '.docusaurus'),
    },
  },
  test: {
    environment: 'jsdom',
    globals: true,
    unstubGlobals: true,
    setupFiles: ['test/setup.ts'],
    include: ['src/**/*.test.{ts,tsx}'],
    coverage: {
      provider: 'v8',
      reporter: ['text', 'html'],
    },
  },
});
