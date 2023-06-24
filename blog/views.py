from django.views import generic
from .models import Post
from django.urls import reverse_lazy
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
import  logging



logger = logging.getLogger(__name__)



class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    # logger.critical(f'MAIN {Post.objects.first()}')



#function based view
#class based view 




#handler/
#formatter
#logger 
#filter

class PostUpdate(generic.UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title','content']
    success_url = reverse_lazy('home')

class PostDelete(generic.DeleteView):
    model = Post
    success_url = reverse_lazy('home')
    template_name = 'post_delete.html'


class PostCreate(generic.CreateView):
    # logger.critical('New post')
    model = Post
    fields = '__all__'
    template_name = 'post_create.html'
    success_url = reverse_lazy('home')

    

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get(self ,request,slug):
        template_name = 'post_detail.html'
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.filter(active=True)
        new_comment = None
        comment_form = CommentForm()
        return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
    
    def post(self,request, slug):
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.filter(active=True)
        new_comment = None
        # Comment posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()

            

        return render(request, self.template_name, {'post': post,
                                            'comments': comments,
                                            'new_comment': new_comment,
                                            'comment_form': comment_form})