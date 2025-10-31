// preload.js
const { exec } = require('child_process');
const path = require('path');
const os = require('os');

window.exports = {
  "blessing_windows": {
    mode: "none",
    args: {
      // 这里可以接收参数，但我们不需要
    },
    fn: () => {
      // 获取Python可执行路径
      const pythonPath = getPythonPath();
      
      // 获取当前插件目录
      const pluginPath = window.utools.getPath('userData') + '/plugins/';
      const scriptPath = path.join(__dirname, 'happy.py');
      
      // 执行Python脚本
      exec(`"${pythonPath}" "${scriptPath}"`, (error, stdout, stderr) => {
        if (error) {
          console.error(`执行错误: ${error}`);
          return;
        }
        if (stderr) {
          console.error(`stderr: ${stderr}`);
        }
        console.log(`stdout: ${stdout}`);
      });
    }
  }
};

// 获取Python路径的辅助函数
function getPythonPath() {
  const platform = os.platform();
  if (platform === 'win32') {
    // Windows系统尝试常见Python安装路径
    return 'python';
  } else {
    // macOS/Linux系统
    return 'python3';
  }
}