/*
 * 实时搜索建议功能
 */

(function() {
  // 等待DOM加载完成
  document.addEventListener('DOMContentLoaded', function() {
    // 找到搜索表单和输入框
    const searchForm = document.getElementById('rtd-search-form');
    const searchInput = searchForm ? searchForm.querySelector('input[name="q"]') : null;
    
    if (!searchInput) return;
    
    // 创建搜索建议容器
    const autocompleteContainer = document.createElement('div');
    autocompleteContainer.id = 'search-autocomplete';
    autocompleteContainer.style.cssText = `
      position: absolute;
      z-index: 1000;
      background: white;
      border: 1px solid #ddd;
      border-radius: 4px;
      max-height: 300px;
      overflow-y: auto;
      width: 100%;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
      display: none;
    `;
    
    // 将容器添加到搜索表单中
    searchForm.appendChild(autocompleteContainer);
    
    // 存储搜索索引
    let searchIndex = null;
    
    // 加载搜索索引
    if (typeof Search !== 'undefined') {
      // 监听搜索索引加载完成
      const originalSetIndex = Search.setIndex;
      Search.setIndex = function(index) {
        searchIndex = index;
        originalSetIndex(index);
      };
    }
    
    // 搜索延迟计时器
    let searchTimer = null;
    
    // 处理输入事件
    searchInput.addEventListener('input', function(e) {
      const query = e.target.value.trim();
      
      // 清除之前的计时器
      if (searchTimer) {
        clearTimeout(searchTimer);
      }
      
      // 如果输入为空，隐藏建议
      if (!query) {
        autocompleteContainer.style.display = 'none';
        return;
      }
      
      // 延迟搜索，避免频繁请求
      searchTimer = setTimeout(function() {
        performSearch(query);
      }, 300);
    });
    
    // 点击页面其他地方时隐藏建议
    document.addEventListener('click', function(e) {
      if (!searchForm.contains(e.target)) {
        autocompleteContainer.style.display = 'none';
      }
    });
    
    // 处理搜索
    function performSearch(query) {
      if (!searchIndex) {
        // 搜索索引尚未加载
        return;
      }
      
      const results = [];
      const queryLower = query.toLowerCase();
      
      // 搜索标题
      const docNames = searchIndex.docnames;
      const titles = searchIndex.titles;
      const allTitles = searchIndex.alltitles;
      
      // 搜索所有标题
      for (const [title, foundTitles] of Object.entries(allTitles)) {
        if (title.toLowerCase().includes(queryLower)) {
          for (const [file, id] of foundTitles) {
            results.push({
              title: titles[file] !== title ? `${titles[file]} > ${title}` : title,
              url: docNames[file] + (id ? '#' + id : ''),
              type: 'title'
            });
          }
        }
      }
      
      // 搜索文件名
      for (let i = 0; i < docNames.length; i++) {
        const docName = docNames[i];
        const title = titles[i];
        if (docName.toLowerCase().includes(queryLower) || title.toLowerCase().includes(queryLower)) {
          results.push({
            title: title,
            url: docName,
            type: 'page'
          });
        }
      }
      
      // 显示结果
      displayResults(results);
    }
    
    // 显示搜索结果
    function displayResults(results) {
      // 清空容器
      autocompleteContainer.innerHTML = '';
      
      if (results.length === 0) {
        autocompleteContainer.style.display = 'none';
        return;
      }
      
      // 创建结果列表
      const ul = document.createElement('ul');
      ul.style.cssText = 'list-style: none; padding: 0; margin: 0;';
      
      // 添加结果项
      results.slice(0, 10).forEach(function(result) {
        const li = document.createElement('li');
        li.style.cssText = 'padding: 8px 12px; cursor: pointer; border-bottom: 1px solid #f0f0f0;';
        li.addEventListener('mouseover', function() {
          li.style.background = '#f5f5f5';
        });
        li.addEventListener('mouseout', function() {
          li.style.background = 'white';
        });
        
        const a = document.createElement('a');
        a.href = result.url + '.html';
        a.textContent = result.title;
        a.style.cssText = 'text-decoration: none; color: #333; display: block;';
        
        li.appendChild(a);
        ul.appendChild(li);
      });
      
      autocompleteContainer.appendChild(ul);
      autocompleteContainer.style.display = 'block';
    }
  });
})();
