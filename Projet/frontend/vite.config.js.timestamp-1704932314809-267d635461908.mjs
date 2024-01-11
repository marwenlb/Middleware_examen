// vite.config.js
import { fileURLToPath, URL } from "node:url";
import { defineConfig, loadEnv } from "file:///home/malabassi/tps/examen-midd/Projet/frontend/node_modules/vite/dist/node/index.js";
import vue from "file:///home/malabassi/tps/examen-midd/Projet/frontend/node_modules/@vitejs/plugin-vue/dist/index.mjs";
var __vite_injected_original_import_meta_url = "file:///home/malabassi/tps/examen-midd/Projet/frontend/vite.config.js";
var vite_config_default = ({ mode }) => {
  const env = loadEnv(mode, "./config");
  return defineConfig({
    plugins: [vue()],
    envDir: "config/",
    resolve: {
      alias: {
        "@": fileURLToPath(new URL("./src", __vite_injected_original_import_meta_url))
      },
      extensions: [".js", ".mjs", ".ts"]
    },
    server: {
      proxy: {
        "/api": {
          target: env.VITE_API_URL,
          changeOrigin: true,
          rewrite: (path) => path.replace(/^\/api/, "")
        }
      }
    }
  });
};
export {
  vite_config_default as default
};
//# sourceMappingURL=data:application/json;base64,ewogICJ2ZXJzaW9uIjogMywKICAic291cmNlcyI6IFsidml0ZS5jb25maWcuanMiXSwKICAic291cmNlc0NvbnRlbnQiOiBbImNvbnN0IF9fdml0ZV9pbmplY3RlZF9vcmlnaW5hbF9kaXJuYW1lID0gXCIvaG9tZS9tYWxhYmFzc2kvdHBzL2V4YW1lbi1taWRkL1Byb2pldC9mcm9udGVuZFwiO2NvbnN0IF9fdml0ZV9pbmplY3RlZF9vcmlnaW5hbF9maWxlbmFtZSA9IFwiL2hvbWUvbWFsYWJhc3NpL3Rwcy9leGFtZW4tbWlkZC9Qcm9qZXQvZnJvbnRlbmQvdml0ZS5jb25maWcuanNcIjtjb25zdCBfX3ZpdGVfaW5qZWN0ZWRfb3JpZ2luYWxfaW1wb3J0X21ldGFfdXJsID0gXCJmaWxlOi8vL2hvbWUvbWFsYWJhc3NpL3Rwcy9leGFtZW4tbWlkZC9Qcm9qZXQvZnJvbnRlbmQvdml0ZS5jb25maWcuanNcIjtpbXBvcnQge2ZpbGVVUkxUb1BhdGgsIFVSTH0gZnJvbSAnbm9kZTp1cmwnXG5cbmltcG9ydCB7ZGVmaW5lQ29uZmlnLCBsb2FkRW52fSBmcm9tICd2aXRlJ1xuaW1wb3J0IHZ1ZSBmcm9tICdAdml0ZWpzL3BsdWdpbi12dWUnXG5cbi8vIGh0dHBzOi8vdml0ZWpzLmRldi9jb25maWcvXG5leHBvcnQgZGVmYXVsdCAoe21vZGV9KSA9PiB7XG4gIGNvbnN0IGVudiA9IGxvYWRFbnYobW9kZSxcIi4vY29uZmlnXCIpXG4gIHJldHVybiBkZWZpbmVDb25maWcoe1xuICAgIHBsdWdpbnM6IFt2dWUoKV0sXG4gICAgZW52RGlyOiBcImNvbmZpZy9cIixcbiAgICByZXNvbHZlOiB7XG4gICAgICBhbGlhczoge1xuICAgICAgICAnQCc6IGZpbGVVUkxUb1BhdGgobmV3IFVSTCgnLi9zcmMnLCBpbXBvcnQubWV0YS51cmwpKVxuICAgICAgfSxcbiAgICAgIGV4dGVuc2lvbnM6IFtcIi5qc1wiLCBcIi5tanNcIiwgXCIudHNcIl0sXG4gICAgfSxcbiAgICBzZXJ2ZXI6IHtcbiAgICAgIHByb3h5OiB7XG4gICAgICAgICcvYXBpJzoge1xuICAgICAgICAgIHRhcmdldDogZW52LlZJVEVfQVBJX1VSTCxcbiAgICAgICAgICBjaGFuZ2VPcmlnaW46IHRydWUsXG4gICAgICAgICAgcmV3cml0ZTogKHBhdGgpID0+IHBhdGgucmVwbGFjZSgvXlxcL2FwaS8sICcnKVxuICAgICAgICB9XG4gICAgICB9XG4gICAgfSxcbiAgfSlcbn1cbiJdLAogICJtYXBwaW5ncyI6ICI7QUFBK1QsU0FBUSxlQUFlLFdBQVU7QUFFaFcsU0FBUSxjQUFjLGVBQWM7QUFDcEMsT0FBTyxTQUFTO0FBSHNMLElBQU0sMkNBQTJDO0FBTXZQLElBQU8sc0JBQVEsQ0FBQyxFQUFDLEtBQUksTUFBTTtBQUN6QixRQUFNLE1BQU0sUUFBUSxNQUFLLFVBQVU7QUFDbkMsU0FBTyxhQUFhO0FBQUEsSUFDbEIsU0FBUyxDQUFDLElBQUksQ0FBQztBQUFBLElBQ2YsUUFBUTtBQUFBLElBQ1IsU0FBUztBQUFBLE1BQ1AsT0FBTztBQUFBLFFBQ0wsS0FBSyxjQUFjLElBQUksSUFBSSxTQUFTLHdDQUFlLENBQUM7QUFBQSxNQUN0RDtBQUFBLE1BQ0EsWUFBWSxDQUFDLE9BQU8sUUFBUSxLQUFLO0FBQUEsSUFDbkM7QUFBQSxJQUNBLFFBQVE7QUFBQSxNQUNOLE9BQU87QUFBQSxRQUNMLFFBQVE7QUFBQSxVQUNOLFFBQVEsSUFBSTtBQUFBLFVBQ1osY0FBYztBQUFBLFVBQ2QsU0FBUyxDQUFDLFNBQVMsS0FBSyxRQUFRLFVBQVUsRUFBRTtBQUFBLFFBQzlDO0FBQUEsTUFDRjtBQUFBLElBQ0Y7QUFBQSxFQUNGLENBQUM7QUFDSDsiLAogICJuYW1lcyI6IFtdCn0K
