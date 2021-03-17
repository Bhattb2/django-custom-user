# ListView, DetailView, DeleteView, CreateView, UpdateView
class SnackListView(ListView):
    template_name = 'snacks/snack-list.html'
    model = Snack

class SnackDetailView(DetailView):
    template_name = 'snacks/snack-detail.html'
    model = Snack

class SnackDeleteView(DeleteView):
    template_name = 'snacks/snack-detail.html'
    model = Snack

class SnackCreateView(CreateView):
    template_name = 'snacks/snack-create.html'
    model = Snack

class SnackUpdateView(UpdateView):
    template_name = 'snacks/snack-update.html'
    model = Snack
