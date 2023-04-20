   def _get(self, *args, **kwargs):
        """
        Get a single list of messages from all storage backends.
        """
        all_messages = []
        for storage in self.storages:
            messages, all_retrieved = storage._get()
            # If the backend hasn't been used, no more retrieval is necessary.
            if messages is None:
                break
            if messages:
                self._used_storages.add(storage)
            all_messages.extend(messages)
            # If this storage class contained all the messages, no further
            # retrieval is necessary
            if all_retrieved:
                break
        return all_messages, all_retrieved


django.db.model query.py

def prefetch_related_objects(model_instances, *related_lookups):
    ...
    my_gen = (args for args in enumerate(through_attrs))
    for level, through_attr in my_gen:
        # Prepare main instances
        ...
        # Prepare objects:
        for obj in obj_list:
            # Since prefetching can re-use instances...
            if not hasattr(obj, "_prefetched_objects_cache"):
                ...
                my_gen.close()

        ...
        # here was clause



django.db.model query.py

def prefetch_related_objects(model_instances, *related_lookups):
    ...
    iterator =
    for level, through_attr in enumerate(through_attrs):
        # Prepare main instances
        ...
        # Prepare objects:
        good_objects = True
        for obj in obj_list:
            # Since prefetching can re-use instances...
            if not hasattr(obj, "_prefetched_objects_cache"):
                ...
                good_objects = False

        ...
        if not good_objects:
            break