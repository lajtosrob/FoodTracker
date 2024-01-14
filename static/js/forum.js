document.addEventListener('DOMContentLoaded', function() {
                    var commentsContainer = document.getElementById('comments-container');
                    var commentText = document.getElementById('comment-text');
                    var postCommentBtn = document.getElementById('post-comment');
                
                    postCommentBtn.addEventListener('click', function() {
                        var comment = commentText.value;
                        if (comment.trim() !== "") {
                            var commentElement = document.createElement('div');
                            commentElement.className = 'comment';
                            commentElement.innerHTML = `
                                <p>${comment}</p>
                                <button class="like-btn">Like</button>
                                <span class="like-count">0</span>
                            `;
                            
                            var likeBtn = commentElement.querySelector('.like-btn');
                            var likeCount = commentElement.querySelector('.like-count');
                            
                            likeBtn.addEventListener('click', function() {
                                var currentLikes = parseInt(likeCount.textContent);
                                likeCount.textContent = currentLikes + 1;
                            });
                
                            commentsContainer.appendChild(commentElement);
                            commentText.value = "";
                        }
                    });
                });